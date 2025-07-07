import openai
import os

def setup_openai():
    """Setup OpenAI API key"""
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("Enter your OpenAI API key:")
        api_key = input("API Key: ").strip()
        
        if not api_key:
            print("No API key provided. Exiting.")
            return False
    
    openai.api_key = api_key
    return True

def ask_gpt(user_input):
    """Send user input to GPT and return response"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[{"role": "user", "content": user_input}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Simple OpenAI CLI Tool")
    print("Type your message and press Enter")
    print("Type 'quit' to exit")
    print("-" * 40)
    
    # Setup OpenAI
    if not setup_openai():
        return
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
            
        print("GPT:", ask_gpt(user_input))

if __name__ == "__main__":
    main() 