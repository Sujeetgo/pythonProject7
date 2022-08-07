import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os


def sptext():
    recogniser = sr.Recognizer
    with sr.Microphone() as source:
        print("Listening..")
        recogniser.adjust_for_ambient_noise(source)
        audio = recogniser.listen(source)
        try:
            print("recognizing...")
            data = recogniser.recognize_google(audio)
            print(data)
            return data

        except sr.UnknownValueError:
            print(" Not understanding.."):

sptext()

def speechtx(x):

    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[0].id )
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)
    engine.say(x)
    engine.runAndWait()
if __name__=='__main__':
    if 'hey peter ' in sptext().lower():
        while True:

            data1 = speechtx().lower()

            if "your name" in data1:
                name = " my name is peter: "
                speechtx(name)
            elif "old are you" in data1:
                age = " i am 2 years old."
                speechtx(age)
            elif 'now time' in data1:
                time = datetime.datetime.now().strftime("%I%M%P")
                speechtx(time)
            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")
            elif 'linkdein' in data1:
                webbrowser.open("https://www.linkedin.com/feed/")
            elif 'jokes' in data1:
                joke_1 = pyjokes.get_joke(language=en,category=neutral)
                print(joke_1)
                speechtx(joke_1)
            elif 'play song' in data1:
                add = " D:\sujeet\song"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os,path.join(add, listsong[0]))

            elif 'exit' in data1:
                speechtx(" thank you")
                break
            time.sleep(10)
            




    else:
      print("thanks")














