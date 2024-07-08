# IntelliLearn

IntelliLearn is a FastAPI-based application designed to process and transcribe audio and video files into text using the Whisper model. The application also supports processing PDF files to extract and summarize their content.

## Features

- Upload audio and video files to convert them to WAV format and transcribe using Whisper.
- Upload PDF files to extract and summarize their content.
- Easy-to-use web interface for file upload and prompt submission.

## Installation

Follow these steps to set up the project:

### Prerequisites

- Python 3.8 or higher
- FFmpeg (for audio/video processing)

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

Ensure you have a `.env` file in the project root with the following variables (do not touch this file):

```
GROQ_API_KEY=your_groq_api_key_here
```

### Run the Application

Use the following command to start the FastAPI application:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

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

## Contributors

This project was developed as part of a graduation project supervised by:

- Dr. Ahmed el Shaer
- Eng. Nagy Khairat
- Eng. Ahmed Metwali

### Collaboration

The following individuals collaborated on this project:

- Ahmed Nasser
- Adham Sherif
- George Youhana
- Magda Elroumany
- Sawsan Kassem
- Sohaila Khaled

## Screenshots

### Home Page
![Home Page](https://via.placeholder.com/800x400?text=Home+Page)

### File Upload
![File Upload](https://via.placeholder.com/800x400?text=File+Upload)

### Results
![Results](https://via.placeholder.com/800x400?text=Results)

## System Architecture

### High-Level Architecture
![System Architecture](https://via.placeholder.com/800x400?text=System+Architecture)

### Data Flow Diagram
![Data Flow Diagram](https://via.placeholder.com/800x400?text=Data+Flow+Diagram)

## Project Impact

IntelliLearn aims to enhance educational experiences by leveraging advanced AI technologies to provide efficient content processing and user-friendly interaction. It bridges the gap between vast information sources and users, facilitating better understanding and retention of complex information.

## Acknowledgments

We would like to express our heartfelt gratitude to the individuals and institutions who have supported and guided us throughout this project. Special thanks to Dr. Ahmed El Shaer for his invaluable mentorship and continuous encouragement, Eng. Nagy Khairat and Eng. Ahmed Metwali for their technical expertise and assistance, and our families and friends for their unwavering support.

---
