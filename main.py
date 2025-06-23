from urllib import response
import speech_recognition as sr
import pyttsx3
import webbrowser
import requests

engine = pyttsx3.init() #initializing pyttsx3

#speak any text aloud
def speak(text):
    engine.say(text)
    engine.runAndWait()

#opens popular websites based on voice command
def social_media(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("Opening Youtube")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        speak("Opening Instagram")

#plays a song using predefined music library
def music_player(c):
    if c.lower().startswith("play"):
        song = c.lower().replace("play", "", 1).strip()
        link = music_library.music[song]
        webbrowser.open(link)
        speak(f"Playing {song}")
    else:
        speak("Song not found in your music library.") 

#fetch and speaks the latest news headlines
def show_news():
    try:
        response = requests.get("NEWS API KEY") 
        news_data = response.json()

        if news_data["status"] == "ok":
            articles = news_data["articles"][:5]  # Limit to top 5 headlines
            speak("Here are the top news headlines.")
            for i, article in enumerate(articles, 1):
                title = article['title']
                description = article.get('description', '')
                speak(f"{i}. {title}")
                print(f"{i}. {title}")
                print(f"   {description}\n")
        else:
            speak("Sorry, I couldn't fetch the news.")
    except Exception as e:
        speak("An error occurred while fetching the news.")
        print("Error:", e)


def process_command(c):
    c = c.lower()
    if "open" in c:
        social_media(c)
    elif "play" in c:
        music_player(c)
    elif "news" in c:
        show_news()
    else:
        speak("I am not sure how to handle that command")

#Jarvis main loop

speak("Initializing jarvis...")

while True:
        s = sr.Recognizer()
        print("Recognizing...")
        
        try:
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = s.listen(source,timeout=3,phrase_time_limit=4)
                    text = s.recognize_google(audio)
                    if text.lower() in ["jarvis","hello jarvis"]:
                        speak("Hello Mister Stark")
                    
                    #listen for command
                    with sr.Microphone() as source:
                        print("Jarvis Active")
                        audio = s.listen(source)
                        command = s.recognize_google(audio)
                        process_command(command)
        except Exception as e:
            print("error;",e)

