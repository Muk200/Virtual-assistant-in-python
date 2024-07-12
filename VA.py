#modeules needed

# pyttsx3 - for text-to-speech conversion is that it works offline.
# SpeechRecognition 
# webbrowser - allows displaying Web-based documents to users.
# wikipedia



import pyttsx3
import speech_recognition as sr
import webbrowser  
import datetime  
import wikipedia 
 

def takeCommand():
 
    r = sr.Recognizer()
 
    # from the speech_Recognition module 

    with sr.Microphone() as source:
        print('Listening')
         
        # seconds of non-speaking audio before 
        
        r.pause_threshold = 0.6
        audio = r.listen(source)
         
        # checks the audio
        try:
            print("Recognizing")
             
            # for hindi recognizing
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
             
        except Exception as e:
            print(e)
            speak("Say that again j")
            return "None"
         
        return Query
 
def speak(audio):
     
    engine = pyttsx3.init()
    
    # getter method, (gets the current value of engine property)
    voices = engine.getProperty('voices')
     
    # setter method,  0 = male, 1 = female
    engine.setProperty('voice', voices[1].id)
     
    # Method for the speaking 
    engine.say(audio)  
     
    # Blocks while processing all the currently queued commands
    engine.runAndWait()
 
def tellDay():
     
    day = datetime.datetime.today().weekday() + 1
     
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
     
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)
 
 
def tellTime():
     
    time = str(datetime.datetime.now())
     
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is" + hour + "Hours and" + min + "Minutes")    
 
def Hello():
     
    speak("hello sir I am your virtual assistant. Tell me how may I help you")
 
 
def Take_query():

    Hello()
     
    # This loop is infinite as it will take unless we do not say bye to exit or terminate the program
    while(True):
         

        query = takeCommand().lower()
        if "open youtube" in query:
            speak("Opening Youtube")
            
            # in the open method we just to give the link of web
            webbrowser.open("www.youtube.com")
            continue
         
        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue
             
        elif "which day it is" in query or "tell day" in query or "tellday" in query or "day" in query:
            tellDay()
            continue
         
        elif "tell me the time" in query or "tell time" in query:
            tellTime()
            continue
         
        # this will exit and terminate the program
        elif "bye" in query or "exit" in query or "b y e" in query or "thank you" in query or "exit the program" in query:
            speak("Goodbye! Have a great day.")
            exit()
            
        elif "from wikipedia" in query or "from wiki" in query:
             
            # if any one wants to have a information from wikipedia
            speak("Checking the wikipedia ")
            query = query.replace("python", "")
             
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(result)
                
            except wikipedia.exceptions.DisambiguationError:
                speak("Multiple matches found. Can you be more specific?")
                
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any information about that.")
         
        elif "tell me your name" in query:
            speak("I am Jarvis. Your desktop Assistant")
            
            
            
        elif "open a website" in query:
            speak("Which website do you want to open? You can choose from YouTube, Steam, Wikipedia, Twitter, Instagram, or ChatGPT.")

            if "youtube" in query:
                webbrowser.open("https://www.youtube.com")
            elif "steam" in query:
                webbrowser.open("https://store.steampowered.com")
            elif "wiki" in query or "wikipedia" in query:
                webbrowser.open("https://www.wikipedia.org")
            elif "twitter" in query:
                webbrowser.open("https://www.twitter.com")
            elif "instagram" in query:
                webbrowser.open("https://www.instagram.com")
            elif "chatgpt" in query or "chat GPT" in query or "chai ki patti" in query:
                webbrowser.open("https://www.chat.openai.com")
                
            elif sr.Recognizer().pause_threshold > 0.6:
                speak("Sorry, that's not a valid option. Please choose from YouTube, Steam, Wikipedia, Twitter, Instagram, or ChatGPT.")

 
if __name__ == '__main__':
     
    # main method for executing the functions
    Take_query()
    r = sr.Recognizer()