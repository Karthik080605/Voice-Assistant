import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import sys


# Initialize the voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Max volume

def speak(text):
    print("🗣️  Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("🧠 You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def greet_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("Hi! I'm your assistant. How can I help you?")

def run_assistant():
    greet_user()
    
    while True:
        command = listen()

        if 'time' in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")

        elif 'date' in command:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")

        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
            
        elif 'open spotify' in command:
            speak("Opening spotify")
            webbrowser.open("https://www.spotify.com")

        elif 'open youtube' in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'play music' in command:
            music_folder = music_folder = r"c:\Users\namei\OneDrive\Music\Playlists"

            try:
                songs = os.listdir(music_folder)
                os.startfile(os.path.join(music_folder, songs[0]))
                speak("Playing music.")
            except Exception:
                speak("Sorry, I couldn't find any music.")

        elif 'exit' in command or 'stop' in command or 'bye' in command:
            speak("Goodbye! Have a nice day.")
            sys.exit()

        elif command != "":
            speak("Sorry, I don't understand that command yet.")
            

# Run the assistant
run_assistant()
