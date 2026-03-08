import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env file
load_dotenv()

# Connect to Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Send a message
question = "Explain what Python is in 2 lines."

response = client.models.generate_content(
    model="gemini-2.0-flash-lite",
    contents=question
)

# Print the response
print(response.text)
