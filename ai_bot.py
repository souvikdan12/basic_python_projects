import speech_recognition as sr
import pyttsx3 as pr
import webbrowser
import os 
import datetime
import time 

# import streamlit as st
# from audiorecorder import audiorecorder

# def laod_assistant():
#     st.title("Bentai Assistant")
#     st.write("Your personal voice assistant. Click on the button below to start recording your command.")
#     audio = audiorecorder("Click to start recording", "Recording... Click to stop")
#     if len(audio) > 0:
#         with open("command.wav", "wb") as f:
#             f.write(audio.tobytes())
#         st.audio(audio.tobytes(), format="audio/wav")

speaker = pr.init()
recongnizer = sr.Recognizer()
mic = sr.Microphone()

def talk(text):
    print(f"Assistant: {text}")
    speaker.say(text)
    speaker.runAndWait()

def take_command():
    try:
        with mic as source:
            print("listening ....")
            
            recongnizer.adjust_for_ambient_noise(source)
            voice = recongnizer.listen(source)
            command = recongnizer.recognize_google(voice, language='en-in')

            return command.lower()
    except Exception as e:
        return "none"
if __name__ == "__main__":
    talk("hello souvik sir  , bentai assisstant here , tell me how can i help you")

    while True:
        text = take_command()
        print(f"you said: {text}")

        if text == "none":
            talk("can you please repeat?")
            continue



        print(f"you said: {text}")
        if "youtube" in text:
            # talk("opening youtube")
            speaker.say("opening youtube")
            webbrowser.open("www.youtube.com")
        
        elif "vs code" in text: 
            # talk("opening vs code")
            speaker.say("opening vs code")
            os.startfile(r"C:\Users\souvi\AppData\Local\Programs\Microsoft VS Code\Code.exe")

            
        elif "open google" in text:
            # talk("opening google")
            speaker.say("opening google")
            webbrowser.open("www.google.com")
            
        elif "close google" in text:
            # talk("closing google")
            speaker.say("closing google")
            os.system("taskkill /im chrome.exe /f")
        
        # elif "bahan chod" in text or "bhen chod" in text or "madarchod" in text or "madrachod" in text or "land" in text or "chutiya" in text or "chutiyapa" in text or "gandu" in text:
        #     # talk("yes souvik i understand gaali but i am not allowed to respond to that")
        #     speaker.say("bhaagg teri maa ki choot")

        # elif "bol bahan ke" in text:
        #     speaker.say("kya bolu be saale ")
        
        elif "microsoft edge" in text:
            # talk("opening microsoft edge")
            speaker.say("opening microsoft edge")
            os.startfile(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

        elif "open gemini" in text:
            # talk("opening gemini")
            speaker.say("opening gemini")
            webbrowser.open("gemini.google.com")
        
        elif "close gemini" in text:
            # talk("closing gemini")
            speaker.say("closing gemini")
            os.system("taskkill /im msedge.exe /f")

        elif "date" in text:
            date = datetime.datetime.now().strftime("%d/%m/%Y")
            # talk(f"souvik today's date is {date}")
            speaker.say(f"souvik today's date is {date}")
        
        elif "who are you" in text or "yourself" in text:
            # talk("I am your personal assistant created by souvik. I am here to make your life easier. You can command me to open applications, search the web, and tell you the date and time.")
            speaker.say("I am your personal assistant created by souvik. I am here to make your life easier. You can command me to open applications, search the web, and tell you the date and time.")
        elif "made" in text or "created" in text:
            #  talk("I was created by souvik.")
            speaker.say("I was created by souvik.")

        elif "your name" in text:
            # talk("My name is bentai assistant.")
            speaker.say("My name is bentai assistant.")

        elif "keep quiet" in text or "be quiet" in text or "shut up" in text or "stop talking" in text or "shant ho jao" in text or "chup raho" in text:
            talk("Okay sir i think you are angry , I will be quiet for few seconds.")
            speaker.say("Okay Sir i think you are angry , I will be quiet for few seconds.")
            time.sleep(10)
            talk("i am back sir , tell me how can i help you")


        elif "joke" in text:
            # talk("Why did the scarecrow win an award? Because he was outstanding in his field!")
            speaker.say("Why did the scarecrow win an award? Because he was outstanding in his field!")
        elif " temperature" in text:
            # talk("The current temperature is 25 degrees Celsius.")
            speaker.say("The current temperature is 25 degrees Celsius.")
        elif "weather" in text:
            # talk("The weather today is sunny with a high of 30 degrees Celsius.")
            speaker.say("The weather today is sunny with a high of 30 degrees Celsius.")
            webbrowser.open("https://www.google.com/search?q=weather+today&sca_esv=aef7960d6ac611d8&rlz=1C1CHBF_enIN1142IN1142&sxsrf=AE3TifPSxsFK49eOtiwHKPBb2FG3BftN2Q%3A1763920485461&udm=50&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZrjP_Cx0LI1Ytb_FGcOviEiTm5uW1q0uNfK7KsnoL8hWZUZ3ZEPhe0cPqXxrOlmBaXNrzSbxDmRd08BPr8JCE3j7NO2M8wRUiHVCUTUzWwSrMdy8mMBaY0wUWGE3eGAC9NQp65Cm5gVSZNebtSuhmGhl1q0GJwZxYY7ZaqJSBd5buhuV7yddXrkE709VeUwSDpH1AiA&aep=1&ntc=1&sa=X&ved=2ahUKEwjpvsrv64iRAxWlaPUHHfsEHiwQ2J8OegQIChAE&biw=1536&bih=730&dpr=1.25&mstk=AUtExfDRiutMR-KgOvKocMjXSXUK3BfM-FOB0qQ-gubZsYutppuyzRyMjpT85e_-Vg5uJ0Zi8GK4DoaPhelJcS8bcPMy1yBLL-FhgdRCOQirPnN9fm_QYd9Iat1YjP2J-gCAjlJa_lTVYY5mOaUidM66vp4hIOVK1pFV50bpbvayEuVt9_P6MlXrsb9I1y74rNXXkCnrYpE-DwmdU_lpktlv9sI5Sc19uH3xgeoSyisNI0DZXee8vZzpVSgeLmlgM_OJhFJo8WZIvn2ePdZThFH_Z1WkBu1mzYKqTd1poPVkxsH738aQeUS9JpiNf6URRuwVfivFCrYTvwnTYQ&csuir=1&mtid=d0ojaYSHIYyaseMPo8vfsQ0")
        elif "news" in text:
            # talk("Here are the latest news headlines.")
            speaker.say("Here are the latest news headlines.")
            webbrowser.open("https://news.google.news.com")
        elif "name" in text:
            # talk("My name is bentai assistant.")
            speaker.say("My name is bentai assistant.")
        elif "time" in text:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            talk(f"souvik the time is {time}")
            speaker.say(f"souvik the time is {time}")
       
        elif "quit" in text or "stop" in text or "exit" in text or "ruko" in text or "band" in text or "ruk ja" in text:

            talk("ok souvik, bye bye")
            speaker.say("ok souvik sir , i would always be here to help you")
            break
