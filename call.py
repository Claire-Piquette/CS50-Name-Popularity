import speech_recognition
import re
import time

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say the name you'd like to us to search for!")
    audio1 = recognizer.listen(source)
    

    print("\nGoogle Speech Recognition thinks you said:")
    print(recognizer.recognize_google(audio1))

    time.sleep(0.75)
    print("Tell us, is this spelled correctly?")
    audio2 = recognizer.listen(source)
    answer = recognizer.recognize_google(audio2)


if re.search("^y(es)?$", answer, re.IGNORECASE):
    name = recognizer.recognize_google(audio1)

elif re.search("^no?$", answer, re.IGNORECASE):
    name = input("Please type out the correct spelling: ")
    name = name.title()



