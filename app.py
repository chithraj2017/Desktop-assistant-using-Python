from src.helper import text_to_speech, speech_to_text, wish
import webbrowser
import wikipedia
import datetime

if __name__ == "__main__":
    #wish the user
    wish()
    query = speech_to_text().lower()
    
    #ask where do want to search or what application to be open
    text_to_speech("where do want to search? or what do you want to do?")
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
    elif 'time' in app:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        text_to_speech(f"The time is {time}")
    else :
        text_to_speech("I will be always there for you...Bye!!!")
    


