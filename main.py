import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser

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

if __name__ == "__main__":
    query = speech_to_text().lower()
    
    if 'wikipedia' in query:
        text_to_speech("Searching in wikipedia")
        answer = wikipedia.summary(query, sentences = 2) # search the query in wikipedia
        print(answer)
        text_to_speech("According to wikipedia")
        text_to_speech(answer)
    elif 'youtube' in query:
        text_to_speech("opening youtube")
        webbrowser.open("https://www.youtube.com/")


