import os
import moviepy.editor as mp
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
from audio_transcription import transcribe_audio
from pdf_processor import preprocess_pdf, parse_pdf_content, paginate_text
from groq_completion import get_groq_completion
import time
import logging

app = FastAPI()

# Load environment variables from .env file
load_dotenv(dotenv_path="file.env")

VALID_VIDEO_EXTENSIONS = {".mp4", ".avi", ".mov", ".flv"}
VALID_AUDIO_EXTENSIONS = {".mp3", ".wav", ".opus"}
VALID_PDF_EXTENSION = ".pdf"

logging.basicConfig(level=logging.INFO)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/upload_form.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    start_time = time.time()
    logging.info("File upload initiated")

    if not file.content_type:
        logging.error("Invalid file type: %s", file.content_type)
        raise HTTPException(status_code=400, detail="Invalid file type")

    try:
        # Save the uploaded file temporarily
        temp_file_path = f"./{file.filename}"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(await file.read())

        save_time = time.time()
        logging.info(f"Time to save file: {save_time - start_time} seconds")

        # Check the file extension
        file_extension = os.path.splitext(temp_file_path)[1].lower()
        if file_extension == VALID_PDF_EXTENSION:
            # Process the PDF file
            file_content = await handle_pdf(temp_file_path)
            file_type = "pdf"
        elif file_extension in VALID_AUDIO_EXTENSIONS and file_extension == ".wav":
            wav_path = temp_file_path
            file_content = await handle_audio(wav_path)
            file_type = "audio"
        elif file_extension in VALID_VIDEO_EXTENSIONS or file_extension in VALID_AUDIO_EXTENSIONS:
            # Convert to WAV if not already a WAV file
            wav_path = convert_to_wav(temp_file_path, temp_file_path.rsplit('.', 1)[0] + ".wav")
            file_content = await handle_audio(wav_path)
            file_type = "video" if file_extension in VALID_VIDEO_EXTENSIONS else "audio"
        else:
            logging.error("Unsupported file type: %s", file_extension)
            raise HTTPException(status_code=400, detail="Unsupported file type")

        process_time = time.time()
        logging.info(f"Time to process file: {process_time - save_time} seconds")

        return {"fileType": file_type, "fileContent": file_content}

    except Exception as e:
        logging.exception("An error occurred during file processing")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        try:
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)
            if 'wav_path' in locals() and os.path.exists(wav_path) and wav_path != temp_file_path:
                os.remove(wav_path)
        except PermissionError:
            pass

    total_time = time.time()
    logging.info(f"Total time: {total_time - start_time} seconds")

async def handle_pdf(file_path: str):
    start_time = time.time()
    logging.info("PDF processing initiated")

    with open(file_path, "rb") as f:
        pdf_bytes = f.read()

    read_time = time.time()
    logging.info(f"Time to read PDF: {read_time - start_time} seconds")

    slides_text = preprocess_pdf(pdf_bytes)
    parsed_content = parse_pdf_content(slides_text)
    chunks = paginate_text(parsed_content, max_tokens=30000)

    preprocess_time = time.time()
    logging.info(f"Time to preprocess PDF: {preprocess_time - read_time} seconds")

    summaries = []
    for chunk in chunks:
        summaries.append(chunk)  # Save the chunks to process with the prompt later

    summarize_time = time.time()
    logging.info(f"Time to summarize PDF: {summarize_time - preprocess_time} seconds")

    combined_content = "\n".join(summaries)
    total_time = time.time()
    logging.info(f"Total time to handle PDF: {total_time - start_time} seconds")

    return combined_content

async def handle_audio(file_path: str):
    start_time = time.time()
    logging.info("Audio processing initiated")

    transcript = transcribe_audio(file_path)

    total_time = time.time()
    logging.info(f"Total time to handle audio: {total_time - start_time} seconds")

    return transcript

def convert_to_wav(in_path, out_path):
    """Convert any video or audio file to WAV format"""
    try:
        clip = mp.VideoFileClip(in_path)
        clip.audio.write_audiofile(out_path, codec='pcm_s16le', fps=clip.audio.fps, nbytes=2)
    except Exception as e:
        logging.exception("Error converting file to WAV")
        raise IOError(f"Error converting file to WAV: {str(e)}")
    return out_path

@app.post("/process_prompt")
async def process_prompt(fileType: str = Form(...), fileContent: str = Form(...), prompt: str = Form(...)):
    start_time = time.time()
    logging.info("Prompt processing initiated")

    if fileType in ["pdf", "audio", "video"]:
        response = await get_groq_completion(prompt + "\n\n" + fileContent)
    else:
        logging.error("Unsupported file type: %s", fileType)
        raise HTTPException(status_code=400, detail="Unsupported file type")

    total_time = time.time()
    logging.info(f"Total time to process prompt: {total_time - start_time} seconds")

    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
