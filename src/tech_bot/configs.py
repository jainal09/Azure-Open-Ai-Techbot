# Use a GPT-4 turbo model
import os

from dotenv import load_dotenv

load_dotenv()

OAI_MODEL = "gpt-4o"
AZURE_DEPLOYMENT = os.getenv("AZURE_DEPLOYMENT")
API_KEY = os.getenv("API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
API_VERSION = os.getenv("API_VERSION")
