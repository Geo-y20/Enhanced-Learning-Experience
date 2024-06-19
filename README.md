
# IntelliLearn

IntelliLearn is a FastAPI-based application designed to process and transcribe audio and video files into text using the Whisper model. The application also supports processing PDF files to extract and summarize their content.

## Features

- Upload audio and video files to convert them to WAV format and transcribe using Whisper.
- Upload PDF files to extract and summarize their content.
- Easy-to-use web interface for file upload and prompt submission.

## Installation

Follow these steps to set up the project:

### Prerequisites

### Create a Virtual Environment

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command to create a virtual environment:

    ```bash
    python -m venv myenv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        myenv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source myenv/bin/activate
        ```

### Install Dependencies

Once the virtual environment is activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

### Environment Variables
we have been creatign file.env ***dont touch it***
### Run the Application

Use the following command to start the FastAPI application:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.


## Note we need to change "Adhaaaam "
- Design of web
- So need to chnage in main .py for rendering page
- Make sure that all packages is good and make  uvicorn main:app --reload for tetsing webpage and complete
- Testing all functionality for check

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:8000`.
2. Use the web interface to upload audio, video, or PDF files.
3. For audio and video files, the application will convert them to WAV format (if necessary) and transcribe the content.
4. For PDF files, the application will extract and summarize the text content.
5. Submit your prompt to process the file content and get the response.

## Project Structure

### `main.py`
The main FastAPI application file. It contains the following endpoints:
- `GET /`: Serves the HTML upload form.
- `POST /upload`: Handles file uploads, processes the files, and converts audio/video files to WAV format if necessary.
- `POST /process_prompt`: Processes the content of the uploaded files based on the provided prompt.

### `audio_transcription.py`
This module contains the `transcribe_audio` function, which uses the Whisper model to transcribe audio files. It includes authentication with Hugging Face and the application of a speaker diarization model.

### `pdf_processor.py`
This module includes functions to preprocess, parse, and paginate PDF files:
- `preprocess_pdf`: Extracts text from each slide of the PDF.
- `parse_pdf_content`: Formats the extracted text into a desired output format.
- `paginate_text`: Splits the text into chunks with a maximum number of tokens.

### `groq_completion.py`
Handles interactions with the Groq API for generating completions based on the provided prompt and content.

### `upload_form.html`
An HTML template for the web interface, allowing users to upload files and submit prompts. It includes:
- A form for uploading files.
- A form for submitting prompts after file upload.
- Loading indicators and result display sections.

### `file.env`
A file to store environment variables, such as the Groq API key. This file should not be included in version control for security reasons.

### `ez_setup.py`
A script to bootstrap the installation of setuptools. It is generally not required if using modern package management practices.

## Running Tests

To run tests, use the following command:

```bash
pytest
```

This will execute any test cases defined for the project.
```

