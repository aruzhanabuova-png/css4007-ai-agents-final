
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key or api_key == "your_api_key_here":
    print("Error: Please add your OpenAI API key to the .env file.")
    raise SystemExit(1)

# Connect to OpenAI
client = OpenAI(api_key=api_key)

print("Welcome to AI Smart Personal Planner!")

user_request = input("What do you want to plan? ")

response = client.responses.create(
    model="gpt-4.1-mini",
    instructions="You are a helpful personal planning assistant. Create clear and practical plans.",
    input=user_request
)

print("\nYour AI Plan:")
print(response.output_text)