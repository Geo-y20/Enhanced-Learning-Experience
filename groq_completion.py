from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path="file.env")

# Debug: Print environment variable value
print("GROQ_API_KEY:", os.environ.get("GROQ_API_KEY"))

async def get_groq_completion(prompt, model="mixtral-8x7b-32768", completion_type="chat"):
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set")

    client = Groq(api_key=api_key)

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model,
        )

        if completion_type == "chat":
            return chat_completion.choices[0].message.content
        else:
            print("Unsupported completion type:", completion_type)
            return None

    except Exception as e:
        print(f"Error with Groq: {e}")
        return None
