 # Main Python file

python
import os
import google.generativeai as genai
from dotenv import load_dotenv

Load API key
load_dotenv()
GENAI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GENAI_API_KEY)

Function to chat with Gemini AI
def chat_with_gemini(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text
 Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat_with_gemini(user_input)
    print("Gemini:", response)

