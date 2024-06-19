from huggingface_hub import login
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set Hugging Face token from environment variable
token = os.getenv("HF_TOKEN")

# Log in using the token
login(token=token)
