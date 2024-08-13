import google.generativeai as genai
import os
import pyttsx3

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model = genai.GenerativeModel('gemini-1.5-flash')
# response = model.generate_content("What is coding",max_tokens= 50)

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# print(response.content)

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Generate content with a word limit
response = model.generate_content("What is coding?")

# Access the generated text
response_text = response.text  # Access the text attribute directly

# Limit the response to 30 words
words = response_text.split()
limited_response = ' '.join(words[:30])

speak(limited_response)