import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime

# Taking pre-built voice from system
engine = pyttsx3.init('sapi5') # Create a new engine instance
voices = engine.getProperty('voices') # get all the voices 
engine.setProperty('voice', voices[1].id)

# Text to Speech function
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

# Speech to text(Speech recoginition) function
def speech_to_text():
    """
    Function to convert a speech into text
    """    
    r = sr.Recognizer() #create an object for recognizer class
    with sr.Microphone() as source:
        print("Listening....")   
        r.pause_threshold = 1    # wait for one sec, otherwise it will recognize noise
        audio =  r.listen(source) # continously listening for audio from microphone

        try:
            print("Recognizing....")
            output_text  = r.recognize_google(audio, language ='en-in') # recognize the text from the audio
            print(output_text)
        except Exception as e:
            print(e)
    return output_text

# Wishing the user

def wish():
    hour = datetime.datetime.now().hour
    if hour>=5 and hour<12:
        text_to_speech("Hi Sir, Good morning. Have a nice day. How can I help you?")
    elif hour>=12 and hour<16:
        text_to_speech("Hi Sir, Good afternoon. What do want to do?")
    elif hour>=16 and hour<23:
        text_to_speech("Hi Sir, Good evening. What do want to do?")
    else:
        text_to_speech("Hi Sir, Good night.")

if __name__ == "__main__":
    #wish the user
    wish()
    query = speech_to_text().lower()
    
    #ask where do want to search or what application to be open
    text_to_speech("where do want to search")
    app = speech_to_text().lower()

    if 'wikipedia' in app:
        text_to_speech("Searching in wikipedia")
        answer = wikipedia.summary(query, sentences = 2) # search the query in wikipedia
        print(answer)
        text_to_speech("According to wikipedia")
        text_to_speech(answer)
    elif 'youtube' in app:
        text_to_speech("opening youtube")
        webbrowser.open("https://www.youtube.com/")


