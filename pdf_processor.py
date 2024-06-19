import io
import pdfplumber

def preprocess_pdf(pdf_bytes: bytes) -> list:
    """
    Preprocesses the PDF file and extracts text from each slide.
    Returns a list of text content for each slide.
    """
    slides_text = []
    with io.BytesIO(pdf_bytes) as pdf_file:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                slides_text.append(text)
    return slides_text

def parse_pdf_content(slides_text: list) -> str:
    """
    Parses the text content of each slide and formats it into the desired output format.
    Returns a formatted string containing the parsed content.
    """
    parsed_content = ""
    for i, slide_text in enumerate(slides_text, start=1):
        parsed_content += f"Slide {i}:\n"
        parsed_content += slide_text.strip() + "\n"
        parsed_content += "=" * 50 + "\n\n"
    return parsed_content

def paginate_text(text: str, max_tokens: int = 30000) -> list:
    """
    Splits the text into chunks with a maximum number of tokens.
    Returns a list of text chunks.
    """
    tokens = text.split()
    chunks = [' '.join(tokens[i:i + max_tokens]) for i in range(0, len(tokens), max_tokens)]
    return chunks

