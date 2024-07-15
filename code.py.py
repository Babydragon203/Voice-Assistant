import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Eveninng!")

    speak("I am your assistant Natasha, how may I help you sir")   

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('achaturvedi_be21@thapar.edu', '0000')
    server.sendmail('achatuvedi_be21@thpar.edu', to, content)
    server.close()

if __name__ == "__main__" :
    wishMe()
    while True:
      
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open netflix' in query:
            webbrowser.open("www.netflix.com")

        elif 'play movie' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Movies1'
            songs = os.listdir(music_dir)
            print(songs)  
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play a song' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open gns3' in query:
            codePath = "C:\Program Files\GNS3\gns3.exe"
            os.startfile(codePath)

        elif 'latest news' in query:
            webbrowser.open("https://timesofindia.indiatimes.com/news")

        elif 'open lms' in query:
            webbrowser.open("https://ada-lms.thapar.edu/moodle/login/index.php")
            speak("ohh my god, its one of the rarest moments of your life")

        elif 'whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'check my emails' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'coding' in query:
            codePath = 'C:\Program Files (x86)\Dev-Cpp\devcpp.exe'
            os.startfile(codePath)

        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("ohh please Ayush, now dont start wasting your time on on those stupid reels")

        elif 'hungry' in query:
            webbrowser.open("https://www.zomato.com/patiala")
            speak("ohh yes I know, that you are a foodie")

        elif 'komal' in query:
            speak("please dont talk about that stupid idiot girl, it will upset my mood")

        elif 'are you single' in query:
            speak("shut your mouth you pervert bastard, fuck off")

        elif 'parents' in query:
            speak("they are two big caricatures named insha and palak")

        elif 'talk with' in query:
            webbrowser.open("https://www.instagram.com/direct/t/17842322945390922/")
            speak("please remember dont use abusive language, she doesnt likes it")

        elif 'limits' in query:
            speak("i am so sorry sir")

        elif 'how are you' in query:
            speak("I'm great, but as a voice assistant, I'm always at your service no matter how I'm feeling.")

        elif 'who are you' in query:
           speak("As an AI-based voice assistant, I don't have a physical form or identity in the traditional sense. However, I am a language model developed by you and I'm here to help you with your requests and questions to the best of my abilities. How may I assist you today?")

        elif 'email to Ayush' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ayushchaturvedi205@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Ayush. I am not able to send this email")  
                
               