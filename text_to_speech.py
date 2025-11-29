import pyttsx3
import time
names = ["Souvik", "Pritam", "sachin","aditya"]

for i in names:
    speaker = pyttsx3.init()
    speaker.say(f"Good morning {i}, how are you bro?")
    speaker.runAndWait()
    time.sleep(2)
    del speaker