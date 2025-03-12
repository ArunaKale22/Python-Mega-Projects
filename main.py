import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import os
import google.generativeai as genai



recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "92b6702695f14a61b761ea3d036a372f"
genai.configure(api_key="AIzaSyAFCb40p1hJvLRoihkPJ2qHIBICqOQ4X44")


def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    model = genai.GenerativeModel("gemini-1.5-flash")  # Use correct model name
    response = model.generate_content(command)
    return response.text
    # print(response.text)  # Print the AI-generated response
    # generate()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            # Extract articles
            articles = data.get("articles", [])
            # Speakout the headlines
            for article in articles:
                speak(article['title'])
    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)
        pass   
        

if __name__ == "__main__":
    speak("Initializing Jarvis....")

    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout = 2, phrase_time_limit = 1)
            word = r.recognize_google(audio)
            if(word.lower() ==  "jarvis"):
                speak("Ya")
                # Listen for the command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))

   