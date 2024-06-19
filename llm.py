import asyncio
from pdf_processor import preprocess_pdf, parse_pdf_content, paginate_text
from groq_completion import get_groq_completion

async def main(pdf_path: str, prompt: str, words_per_line: int = 50):
    # Read and preprocess the PDF
    with open(pdf_path, 'rb') as f:
        pdf_bytes = f.read()

    slides_text = preprocess_pdf(pdf_bytes)
    parsed_content = parse_pdf_content(slides_text)

    # Paginate text with a larger chunk size
    chunks = paginate_text(parsed_content, max_tokens=30000)  # Increased chunk size to 30,000 tokens

    # Summarize each chunk and combine summaries
    summaries = []
    for chunk in chunks:
        response = await get_groq_completion(prompt + "\n\n" + chunk)
        summaries.append(response)

    combined_summary = "\n".join(summaries)

    # Final summary if the combined summary is too long
    if len(combined_summary.split()) > 1000:  # Assuming 1000 words as the final summary limit
        combined_summary = await get_groq_completion("summarize this: \n\n" + combined_summary)

    # Calculate number of lines based on words_per_line
    words = combined_summary.split()
    lines = [' '.join(words[i:i+words_per_line]) for i in range(0, len(words), words_per_line)]

    # Print the lines one by one
    for line in lines:
        print(line)

if __name__ == "__main__":
    pdf_path = r"C:\Users\Mega\Downloads\End Point\George Youhana Resume.pdf"  # Specify the path to your PDF file
    prompt = "summarize this cv"  # Specify your desired prompt
    words_per_line = 50  # Number of words per line

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(pdf_path, prompt, words_per_line))
