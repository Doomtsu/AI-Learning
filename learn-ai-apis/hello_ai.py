import openai
import os
from dotenv import load_dotenv

# Load .env file and API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the function to send prompt to GPT
def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or use "gpt-3.5-turbo" if you prefer
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# Command line chat loop
if __name__ == "__main__":
    print("ChatGPT CLI is running. Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        print("GPT:", ask_gpt(user_input))

