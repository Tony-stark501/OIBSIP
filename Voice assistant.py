import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 16:
        speak("Good afternoon!")
    else:
        speak("Good evening!")



def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("User:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        return ""

def search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def main():
    greet()
    speak("How can I assist you today?")

    while True:
        query = listen()

        if "hello" in query:
            speak("Hello! How can I help you?")
        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
        elif "date" in query:
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak(f"Today is {current_date}")
        elif "search" in query:
            query = query.replace("search", "").strip()
            if query:
                search(query)
            else:
                speak("What do you want me to search for?")
        elif "exit" in query or "quit" in query:
            speak("Goodbye!,Have a great day!")
            break

if __name__ == "__main__":
    main()
