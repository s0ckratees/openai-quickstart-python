import os
import openai
import sys
from dotenv import load_dotenv


load_dotenv()
# Load your API key from an environment variable or secret management service

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "tagline for a curly haircare store"

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt,
 #  temperature=0.8,
  max_tokens=10,
 # top_p=1.0,
 # frequency_penalty=0.0,
 # presence_penalty=0.0,
 # stop=["\n"]
)

print(response)