import speech_recognition as sr
import webbrowser
import pyttsx3
import pocketsphinx
import music_library
import google.generativeai as genai
import os
import datetime
import wikipedia

# recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(command)
    response_text = response.text  # Access the text attribute directly

    # Limit the response to 30 words
    words = response_text.split()
    limited_response = ' '.join(words[:30])

    return limited_response

def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google..")
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook..")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        speak("Opening Youtube..")
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        speak("Opening Instagram..")
        webbrowser.open("https://instagram.com")
    elif "open linkeden" in c.lower():
        speak("Opening Linkeden..")
        webbrowser.open("https://linkeden.com")
    elif "open github" in c.lower():
        speak("Opening Github..")
        webbrowser.open("https://github.com")
    elif "open chatgpt" in c.lower():
        speak("Opening Chatgpt..")
        webbrowser.open("https://chatgpt.com/")
    elif "open gemini" in c.lower():
        speak("Opening Gemini..")
        webbrowser.open("https://gemini.google.com/")
    elif 'wikipedia' in c.lower():
        speak('Searching Wikipedia...')
        query = c.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link) 
    elif 'the time' in c.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")
    else:
        output = aiprocess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    #Listen for the wake word Jarvis
    # obtain audio from the microphone
    while True:
        r = sr.Recognizer()

        print("Recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=3,phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Ya")

                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source,timeout=3,phrase_time_limit=4)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))