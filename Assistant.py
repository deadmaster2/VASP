import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import os
from googlesearch import *
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Vasp! Please tell me how may I help you?")

def TakeCommand():
    #It takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 600
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query1 = r.recognize_google(audio, language='en-in')
        print(f"User said: {query1}\n")
    except Exception as e:
        #print(e)
        speak("Say that again please!")

    return query1

def open_application(query1):

    if 'chrome' in query1:
        speak("Opening google chrome...")
        os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    elif 'pycharm' in query1:
        speak("Opening pycharm...")
        os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.3\\bin\\pycharm64.exe")
    elif 'word' in query1:
        speak("Opening MS word...")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk")
    elif 'powerpoint' in query1:
        speak("Opening MS Powerpoint...")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft PowerPoint Word 2007.lnk")
    elif 'movies' in query1:
        speak("Opening movies folder...")
        os.startfile("C:\\Ankit\\Movies & Series")
    elif 'calculator' in query1:
        speak("Opening Calculator...")
        os.startfile("C:\\Windows\\System32\\calc.exe")
    elif 'vlc' in query1:
        speak("Opening vlc...")
        os.startfile("C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe")
    else:
        speak("Application not available!!")

def Operation():
    while True:
        query1 = TakeCommand().lower()
        #Logic for executing tasks based on query1

        if 'wikipedia' in query1 or 'wiki' in query1:
            speak("Searching Wikipedia...")
            query1 = query1.replace("wikipedia", "")
            results = wikipedia.summary(query1, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query1:
            webbrowser.open("http://www.youtube.com")
            speak("Opening YouTube...")

        elif 'geeksforgeeks' in query1:
            webbrowser.open("http://www.geeksforgeeks.com")
            speak("Opening geeksforgeeks...")

        elif 'stackoverflow' in query1:
            webbrowser.open("http://www.stackoverflow.com")
            speak("Opening stackoverflow...")

        elif 'the time' in query1:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'play music' in query1:
            music_dir = 'C:\\Ankit\\Music'
            songs = random.choice(os.listdir(music_dir))
            print(songs)
            os.startfile(os.path.join(music_dir, songs))
            speak("Playing songs...")

        elif 'search' in query1:
            speak('Searching Google...')
            query1 = query1.replace("search", "")
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            for url in search(query1, tld="co.in", num=1, stop=1, pause=2):
                webbrowser.open("https://google.com/search?q=%s" % query1)

        elif 'joke' in query1:
            path = 'C:\\Ankit\\Jokes\\'
            def getRandom():
                file = random.choice(os.listdir(path))
                print(file)
                joke = open(path + file)
                content = joke.read()
                print(content)
                joke.close()
                return content
            speak(getRandom())

        elif 'open' in query1 or 'launch' in query1:
            open_application(query1)

        elif 'who are you' in query1 or 'tell me about' in query1:
            speak("Hello, I am Vasp. Your personal Assistant. I am here to help you to perform various operations.")

        elif 'quit' in query1 or 'exit' in query1 or 'stop' in query1:
            speak("Yes, i will be powering off, hope you enjoyed talking with me!")
            exit(0)

        elif 'goodbye' in query1 or 'good bye' in query1:
            speak("Yes, i will be powering off, hope you enjoyed talking with me!")
            exit(0)

        elif "calculate" in query1:

            # write your wolframalpha app_id here
            app_id = "KUVQQY-LYUPTQAK3G"
            client = wolframalpha.Client(app_id)

            indx = query1.lower().split().index('calculate')
            query = query1.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            #print(answer)
            speak("The answer is " + answer)

        elif "what is" in query1 or "where is" in query1 or "how is" in query1:

            # write your wolframalpha app_id here
            app_id = "KUVQQY-LYUPTQAK3G"
            client = wolframalpha.Client(app_id)

            #indx = query1.lower().split().index('what is')
            #query = query1.split()[indx + 1:]
            res = client.query(query1)
            answer = next(res.results).text
            print(answer)
            speak(answer)


        else:
            speak("I am not sure I can help you here, should I find something on internet?")
            input = TakeCommand().lower()
            if 'yes' in input or 'yeah' in input:
                chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                for url in search(query1, tld="co.in", num=1, stop=1, pause=2):
                    webbrowser.open("https://google.com/search?q=%s" % query1)


if __name__ == '__main__':
    WishMe()
    Operation()