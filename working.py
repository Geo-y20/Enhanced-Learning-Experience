from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from dotenv import load_dotenv
from pdf_processor import preprocess_pdf, parse_pdf_content, paginate_text
from audio_transcription import transcribe_audio
from groq_completion import get_groq_completion
import time

app = FastAPI()

# Load environment variables from .env file
load_dotenv(dotenv_path="file.env")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/upload_form.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.post("/upload")
async def upload_file(fileType: str = Form(...), file: UploadFile = File(...)):
    start_time = time.time()

    if not file.content_type:
        raise HTTPException(status_code=400, detail="Invalid file type")

    try:
        # Save the uploaded file temporarily
        temp_file_path = f"./{file.filename}"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(await file.read())
        
        save_time = time.time()
        print(f"Time to save file: {save_time - start_time} seconds")

        # Dispatch to the corresponding function based on the file type
        if fileType == "pdf":
            file_content = await handle_pdf(temp_file_path)
        elif fileType == "audio":
            file_content = await handle_audio(temp_file_path)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")

        process_time = time.time()
        print(f"Time to process file: {process_time - save_time} seconds")

        return {"fileType": fileType, "fileContent": file_content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        try:
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)
        except PermissionError:
            pass

    total_time = time.time()
    print(f"Total time: {total_time - start_time} seconds")

async def handle_pdf(file_path: str):
    start_time = time.time()

    with open(file_path, "rb") as f:
        pdf_bytes = f.read()
    
    read_time = time.time()
    print(f"Time to read PDF: {read_time - start_time} seconds")

    slides_text = preprocess_pdf(pdf_bytes)
    parsed_content = parse_pdf_content(slides_text)
    chunks = paginate_text(parsed_content, max_tokens=30000)
    
    preprocess_time = time.time()
    print(f"Time to preprocess PDF: {preprocess_time - read_time} seconds")

    summaries = []
    for chunk in chunks:
        summaries.append(chunk)  # Save the chunks to process with the prompt later
    
    summarize_time = time.time()
    print(f"Time to summarize PDF: {summarize_time - preprocess_time} seconds")

    combined_content = "\n".join(summaries)
    total_time = time.time()
    print(f"Total time to handle PDF: {total_time - start_time} seconds")

    return combined_content

async def handle_audio(file_path: str):
    start_time = time.time()

    transcript = transcribe_audio(file_path)
    
    total_time = time.time()
    print(f"Total time to handle audio: {total_time - start_time} seconds")

    return transcript

@app.post("/process_prompt")
async def process_prompt(fileType: str = Form(...), fileContent: str = Form(...), prompt: str = Form(...)):
    start_time = time.time()

    if fileType == "pdf" or fileType == "audio":
        response = await get_groq_completion(prompt + "\n\n" + fileContent)
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    total_time = time.time()
    print(f"Total time to process prompt: {total_time - start_time} seconds")

    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
