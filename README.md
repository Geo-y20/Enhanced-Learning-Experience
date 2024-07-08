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

## Getting the Groq API Key

To obtain a Groq API key, follow these steps:

1. Visit the [Groq Cloud website](https://groq.com/cloud).
2. Sign up for an account or log in if you already have one.
3. Navigate to the API section in your account dashboard.
4. Generate a new API key and copy it.
5. Add the API key to your `.env` file in the project root as follows:

    ```
    GROQ_API_KEY=your_groq_api_key_here
    ```

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
![Home Page](https://github.com/Geo-y20/IntelliLearn/blob/main/Photos%20Sample%20Website/home.JPG)

### About Page
![About Page](https://github.com/Geo-y20/IntelliLearn/blob/main/Photos%20Sample%20Website/about.JPG)

### File Upload
![File Upload](https://github.com/Geo-y20/IntelliLearn/blob/main/Photos%20Sample%20Website/upload.JPG)

### Results
![Results](https://github.com/Geo-y20/IntelliLearn/blob/main/Photos%20Sample%20Website/results.JPG)

## System Architecture

### High-Level Architecture
![System Architecture](https://github.com/Geo-y20/IntelliLearn/blob/main/Diagrams/model.JPG)

### Data Flow Diagram
![Data Flow Diagram](https://github.com/Geo-y20/IntelliLearn/blob/main/Diagrams/preprocessing%20schema.JPG)

## Demonistartion 
![Demonistartion](https://github.com/Geo-y20/IntelliLearn/blob/main/Diagrams/demonistartion.JPG)

## Conclusion

In this project, we developed "IntelliLearn," an advanced AI system designed to enhance content accessibility and comprehension through sophisticated text analysis, summarization, and generation. By integrating cutting-edge technologies such as OpenAI's Whisper and xAI's Grok, IntelliLearn processes a wide variety of content types, including PDFs, images, audio files, and videos. Leveraging state-of-the-art NLP and machine learning techniques, IntelliLearn facilitates better understanding and retention of complex information. The system effectively bridges the gap between vast information sources and users, providing a user-friendly interface and robust educational support. IntelliLearn not only enhances the accessibility of educational content but also streamlines the process of information extraction and utilization, thereby significantly contributing to the field of educational technology.

## Future Work

1. **Integration of Additional Language Models**:
   - Incorporate more advanced language models and domain-specific knowledge bases to enhance performance and context awareness.
   - Explore the integration of multilingual support to cater to a broader audience.

2. **Reinforcement Learning for Optimization**:
   - Investigate the application of reinforcement learning techniques to optimize text summarization and generation processes.
   - Utilize reinforcement learning to adapt and improve model responses based on user interactions and feedback.

3. **Enhanced Accessibility Features**:
   - Develop and implement additional accessibility features to support users with disabilities, ensuring inclusivity.
   - Gather comprehensive user feedback to identify areas for improvement and iteratively enhance the system’s usability.

4. **Advanced Video Summarization**:
   - Expand the system’s capabilities to include video summarization, allowing users to extract key information from educational videos efficiently.
   - Implement lecture summary functionalities to assist students in reviewing and understanding lecture content.

5. **Visual Aids Generation**:
   - Develop tools to automatically generate visual aids such as charts, graphs, and infographics from text content, aiding visual learners.
   - Enhance the system’s ability to create interactive and engaging educational materials.

6. **User-Centric Enhancements**:
   - Continuously refine the user interface based on user experience research to ensure it remains intuitive and user-friendly.
   - Introduce personalized learning paths and recommendations based on user performance and preferences.

7. **Scalability and Performance Improvements**:
   - Invest in scalable cloud infrastructure to handle increasing data volumes and user load without compromising performance.
   - Optimize algorithms for faster processing times and lower latency in real-time applications.

8. **Compliance and Security Enhancements**:
   - Ensure ongoing compliance with data protection regulations (e.g., GDPR, CCPA) to maintain user trust and data security.
   - Implement advanced security measures to protect user data during transmission, processing, and storage.

9. **Educational Partnerships**:
   - Collaborate with more educational institutions to integrate IntelliLearn into their systems, tailoring solutions to meet specific needs.
   - Establish partnerships with educational content creators to expand the range of supported materials.

10. **Comprehensive Evaluation and Benchmarking**:
    - Conduct extensive evaluations and benchmarking against existing educational tools to continuously measure and improve IntelliLearn’s effectiveness.
    - Publish findings in academic and industry forums to contribute to the broader field of educational technology.


## Video Demonstration

To better understand how IntelliLearn works and see it in action, you can watch our detailed video demonstration. The video covers the following aspects:

- Overview of IntelliLearn and its features
- Step-by-step guide on how to upload and process files
- Examples of audio, video, and PDF file processing
- Transcription and summarization outputs
- Insights into the system architecture and data flow

[![Graduation Project Video](https://github.com/Geo-y20/IntelliLearn/blob/main/Photos%20Sample%20Website/home.JPG)](https://github.com/Geo-y20/IntelliLearn/blob/main/Final%20Video%20Graduation%20Project.mp4)
