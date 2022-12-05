import speech_recognition as sr

r = sr.Recognizer()

def recognize():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening....")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")
        except sr.UnknownValueError:
            print("Could not understand audio")
            return