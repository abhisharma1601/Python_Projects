import tkinter as tk
from PIL import ImageTk,Image
import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
from random import randint

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning sir!Snappy here")
    elif 12 <= hour < 15:
        speak("Good afternoon sir!Snappy here")
    else:
        speak("Good Evening sir!Snappy here")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning...")
        r.pause_threshold = 1  # time of speaking
        audio = r.listen(source)
        try:
            os.system("cls")
            print("recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print("User said\n{}".format(query))
        except:
            print("Unable to Communicate")
    return query

def follow():
    speak("How can i help you?")
    while True:
        command = take_command().lower()
        if "wikipedia" in command:
            speak("searching wikipedia")
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences="2")
            speak("According to wikipedia")
            speak(results)
            break
        elif "visit" in command:
            command = command.replace("visit","")
            command = command[1:len(command)]
            webbrowser.open("{}.co.in".format(command))
            break
        elif "play music" in command:
            num = randint(0, 8)
            dir = "C:\\Users\\ABHISHEK SHARMA\\Desktop\\songs"
            songs = os.listdir(dir)
            os.startfile(os.path.join(dir, songs[num]))
            break
        elif "time" in command:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(time)
            break
        elif "shutdown" in command:
            speak("are you sure")
            cmd = take_command()
            if "yes" in cmd:
                os.system("shutdown /s /t 1")
                break
        elif "dark music" in command:
            webbrowser.open("darkmusic.online")
            break
        elif "spotify" in command:
            dir = "C:\\Users\\ABHISHEK SHARMA\\AppData\Roaming\\Spotify\\Spotify.exe"
            os.startfile(os.path.join(dir))
            break
        elif "close yourself" in command:
            speak("thank you for using me!have a good day")
            root.destroy()
            break
        else:
            break


root =tk.Tk()
root.title("Snappy A.I.")
canvas = tk.Canvas(root,height='451',width='480',command = wish_me())
canvas.pack()
pic = ImageTk.PhotoImage(Image.open('1.png'))
pic1= ImageTk.PhotoImage(Image.open('12.png'))
label = tk.Label(canvas,image = pic)
label.pack()
main_button = tk.Button(text="Start",command = follow)
main_button.place(relheight='0.1',relwidth='0.1',relx=0.75,rely=0.7)
root.mainloop()