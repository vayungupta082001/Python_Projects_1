import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import calendar
import wikipedia
import pyjokes
import os
import pywhatkit
import smtplib
import config3
import config2
from tkinter import*
import pyautogui
from nothing import ps
import time
import light_control as lc

global passkey
passkey = ps

e = pyttsx3.init("sapi5")
voice = e.getProperty("voices")
e.setProperty("voices",voice[1].id)
print(voice[1].id)


while True:

    def wake_upp():
        while True:
            q=comm().lower()
            if "wake up jarvis" in q or "jarvis wake up" in q or ("wake up" in q and "jarvis" in q):
                speak("Yes sir, I am Awake")
                break

    def Light_On():
        speak("Which one sir?")
        i=comm().lower()
        if i=="lite 1" or i=="light 1" or i=="light one"  or i=="lite one" or i== "1" or i=="one" or i=="2" or i=="two":
            k='1'
            lc.Light_on(k)
            speak("Light 1 is now ON, Sir")
            

        elif i=="lite 2" or i=="light 2" or i=="light two" or i=="lite two" or i== "1" or i=="one" or i=="2" or i=="two":
            k='1'
            lc.Light_on(k)
            speak("Light 2 is now ON, Sir")
        else:
            speak("Ok, As you wish!!, sir")
            pass

    def Light_off():
        
        speak("Which one sir?")
        i = comm().strip()
        if i=="lite 1" or i=="light 1" or i=="light one"  or i=="lite one" or i== "1" or i=="one" or i=="2" or i=="two":
            k='0'
            lc.Light_off(k)
            speak("Light 1 is now OFF, Sir")

        elif i=="lite 2" or i=="light 2" or i=="light two" or i=="lite two" or i== "1" or i=="one" or i=="2" or i=="two":
            k='0'
            lc.Light_off(k)
            speak("Light 2 is now OFF, Sir")

    def shutdown_laptop():
        speak("Enter the passkey")
        ui = str(input("Enter The pass key(hint: nothing.py) : "))
        if (ui==passkey):
            
            pywhatkit.shutdown(time=10)
            exit()

        elif (ui=="quit"):
            pass  

    def send_email(subject,add, msg):
        try:
            server = smtplib.SMTP("smtp.gmail.com:587")
            server.ehlo()
            server.starttls()
            server.login(config2.EMAIL_ADDRESS, config2.PASSWORD)
            message = "Subject: {}\n\n{}".format(subject, msg)
            server.sendmail(config2.EMAIL_ADDRESS, add, message)
            server.quit()
            print("Success: Email sent")
                    
        except:
            print("Email failed to send.") 


    def tellDay():
        day = datetime.date.today()
        speak(calendar.day_name[day.weekday()])
    
    def tellTime():
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        output = "Your current local time is ",current_time
        speak(output)

    def speak(audio):
        e.say(audio)
        print(audio)
        e.runAndWait()

    def comm():
        r = sr.Recognizer()
        print("listening....")
        with sr.Microphone() as source:
            r.pause_threshold = 3
            audio = r.listen(source=source, timeout=5,phrase_time_limit=5)
            r.adjust_for_ambient_noise(source=source)

        try:
            print("Recognizing")
            q = r.recognize_google(audio,language="en-IN")
            print(f"user said: {q}")

        except Exception as ex:
            return "none"
        return q

    def wish():
        h = (datetime.datetime.now().hour)

        if h>=0 and h<=12:
            speak("Good Morning")
        elif h>12 and h<17:
            speak("Good Afternoon")
        else:
            speak("Good Evening")
        speak("I am jarvis sir your desktop assistant. Please tell how may i help you?")

    if __name__=="__main__":
        wish()
        while True:
            q=comm().lower()

            if "wake up jarvis" in q:
                speak("Yes sir, I am Awake")

            if "jarvis"in q or "javed"in q or "java" in q:

                

                if "turn on the lights" in q or "turn on the light" in q or "lights on" in q or "light on" in q or "on light " in q or "on lights" in q or "lights turned on" in q or "on the lights" in q or "switch on the lights " in q or "switch on the light" in q or "switch on light" in q or "switch on lights" in q or "on the light"in q:
                    Light_On()
                elif "turn off the lights" in q or "turn off the light" in q or "lights off" in q or "light off" in q or "off light " in q or "off lights" in q or "lights turned off" in q or "off the lights" in q or "switch off the lights " in q or "switch off the light" in q or "switch off light" in q or "switch off lights" in q or "off the light"in q:
                    Light_off()

                elif "open notepad" in q:
                    path ="C:\\WINDOWS\\system32\\notepad.exe"
                    speak("opening notepad")
                    os.startfile(path)

                elif "sleep" in q:
                    speak("ok, sir")
                    wake_upp()
                    
                elif "open code" in q:
                    codePath = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
                    os.startfile(codePath)
                    speak("opening Visual Studio Code")

                elif "time" in q:
                    tellTime()
                     

                elif "day" in q:
                    tellDay()
                     
                    continue

                elif "goodbye" in q:
                    speak("Good Bye sir!")
                     
                    exit()

                elif "get lost" in q:
                    speak("Sir, That was rude")
                     
                    exit()

                elif "shut up" in q:
                    speak("Sir, that was too rude!")
                     
                    exit()

                elif "youtube" in q:
                     
                    speak("Opening youtube ")
                    webbrowser.open("www.youtube.com")

                elif "switch off the laptop" in q:
                    shutdown_laptop()

                elif "shutdown the laptop" in q:
                    shutdown_laptop()

                elif "open google" in q:
                    speak("Opening Google Chrome ")
                     
                    webbrowser.open("www.google.com")

                elif "from wikipedia" in q:
                    speak("Checking the wikipedia ")
                     
                    qu = q.replace("wikipedia", "")
                    qu = q.replace("jarvis", "")
                    result = wikipedia.summary(qu, sentences=4)
                    speak("According to wikipedia")
                    speak(result)
                    print(result)

                elif "introduce yourself" in q:
                    speak("I am Jarvis. Your Virtual Assistant!")
                     
                    
                elif "joke" in q:
                    speak(pyjokes.get_joke())
                     

                elif "whatsapp message to mum" in q:
                    current_min= datetime.datetime.now().min#int(input("Please say the minute in which i have to send: "))   #datetime.datetime.now().minute
                    current_hr=datetime.datetime.now().hour#int(input("Please say the hour in 24 hrs format in which i have to send: "))#datetime.datetime.now().hour
                    speak("what should i say")
                    w=input("What shold i write: ")
                    pywhatkit.sendwhatmsg("+91 8910943314",w,current_hr,current_min+2)
                    speak("Sending Whatsapp msg to mom")

                elif "song" in q:
                    speak("which song(please write)?")
                    s = input("Which song(pls write): ")
                    speak(f"playing {s}")
                    pywhatkit.playonyt(s)

                elif "who made you" in q:

                    creator_age = (datetime.datetime.now().year)-2010
                    speak(f"A person named Vayun Gupta is who made me, his age is {creator_age}. He made me and let me live!!")

                elif "open microsoft teams" in q:
                    codePath = "C:\\Users\\DELL\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
                    os.startfile(codePath)
                    speak("opening Microsoft Teams")

                elif "microsoft edge"in q:
                    codePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                    os.startfile(codePath)
                    speak("opening Microsoft Edge")

                elif "open command prompt" in q or "cmd" in q:
                    codePath = input("pls enter the path : ")
                    os.startfile(codePath)
                    speak("opening Command Prompt")
                    speak("You can access the command promt only after typing cmd in the path area.")

                elif "play your and my favourite song" in q:
                    song = "See You Again"
                    speak(f"playing {song}")
                    pywhatkit.playonyt(song)

                elif "instagram" in q:
                     
                    speak("Opening instagram ")
                    webbrowser.open("www.instagram.com")

                elif "facebook" in q:
                     
                    speak("Opening facebook ")
                    webbrowser.open("www.facebook.com")
                    
                elif "video" in q:
                    speak("which video(please write)?")
                    s = input("Which video(pls write): ")
                    speak(f"playing {s} on youtube")
                    pywhatkit.playonyt(s)

                elif "whatsapp" in q:
                     
                    speak("Opening whatsapp ")
                    webbrowser.open("https://web.whatsapp.com/")

                elif "filmora" in q:
                    path ="C:\\Program Files\\Wondershare\\Filmora9\\Filmora.exe"
                    speak("opening Filmora")
                    os.startfile(path)

                elif "free cam 8" in q:                               
                    path ="C:\\Program Files (x86)\\Free Cam 8\\freecam.exe"
                    speak("opening FreeCam8")
                    os.startfile(path)

                elif "arduino" in q:
                    path ="C:\\Program Files (x86)\\Arduino\\arduino.exe"
                    speak("opening Aurduino Builder")
                    os.startfile(path)

                elif "any desk" in q or"anydesk"in q:
                    path ="C:\Program Files (x86)\AnyDesk\AnyDesk.exe"
                    speak("opening Anydesk")
                    os.startfile(path)

                elif "open scratch desktop" in q:       
                    path ="C:\\Program Files (x86)\\Scratch Desktop\\Scratch Desktop.exe"
                    speak("opening scratch desktop")
                    os.startfile(path)

                elif "my virus protector" in q:
                    path ="C:\\Program Files\\AVAST Software\\Avast\\AvastUI.exe"
                    speak("opening Avast Free Antivirus")
                    os.startfile(path)

                elif "shut down" in q or "shutdown" in q:
                    speak("Switching off sir")
                     
                    exit()
                
                elif "whatsapp to mom" in q:
                    current_min=int(input("Please say the minute in which i have to send: "))   #datetime.datetime.now().minute
                    current_hr=int(input("Please say the hour in 24 hrs format in which i have to send: "))#datetime.datetime.now().hour
                    speak("what should i say")
                    w=input("What shold i write: ")
                    pywhatkit.sendwhatmsg("+91 98362 33686",w,current_hr,current_min+2)
                    speak("Sending Whatsapp msg to mom")

                elif "whatsapp to sniggy" in q:
                    current_min=int(input("Please say the minute in which i have to send: "))   #datetime.datetime.now().minute
                    current_hr=int(input("Please say the hour in 24 hrs format in which i have to send: "))#datetime.datetime.now().hour
                    speak("what should i say")
                    w=input("What shold i write: ")
                    pywhatkit.sendwhatmsg("+91 79805 17250",w,current_hr,current_min+2)
                    speak("Sending Whatsapp msg to mom")

                elif "whatsapp to father" in q:
                    current_min=int(input("Please say the minute in which i have to send: "))   #datetime.datetime.now().minute
                    current_hr=int(input("Please say the hour in 24 hrs format in which i have to send: "))#datetime.datetime.now().hour
                    speak("what should i say")
                    w=input("What shold i write: ")
                    pywhatkit.sendwhatmsg("+917903060471 ",w,current_hr,current_min+2)
                    speak("Sending Whatsapp msg to father")

                elif "discord" in q:       
                    path ="C:\\Users\\DELL\\AppData\\Local\\Discord\\app-1.0.9002\\Discord.exe"
                    speak("opening discord")
                    os.startfile(path)

                elif "open" in q and "gmail" in q:
                    print(f"user: {q}")
                    webbrowser.open("www.gmail.com")
                    speak("Opening G-mail")

                elif "open google" in q:
                    print(f"user: {q}")
                    webbrowser.Chrome.open("www.google.com")
                    speak("Opening Google")

                elif "send" in q and "gmail" in q:
                    print(f"User:{q}")
                    address=input("Enter the Address : ")

                elif "mail to my mum" in q:
                    subject = input("Write the subject: ")
                    msg = input("Write the message: ")
                    
                    send_email(subject,config3.Mom_email, msg)

                elif "mail to vayu" in q:
                    subject = input("Write the subject: ")
                    msg = input("Write the message: ")
                    
                    send_email(subject,config3.vayun_email, msg)

                elif "through mail address" in q:
                    m = input("Write the mail: ")
                    subject = input("Write the subject: ")
                    msg = input("Write the message: ")

                    send_email(subject,m, msg)

                elif "mail to my sister" in q:
                    subject = input("Write the subject: ")
                    msg = input("Write the message: ")
                    
                    send_email(subject, config3.sniggy_email, msg)

                elif "mail to coding bhaiya" in q:
                    subject = input("Write the subject: ")
                    msg = input("Write the message: ")
                    
                    send_email(subject, config3.Coding_Bhaia, msg)

                elif "minecraft in browser" in q:
                     
                    webbrowser.open("https://minecraft-js.vercel.app/")
                    speak("Opening Minecraft in Browser")

                elif "mail to my father" in q:
                    subject = input("Write the subject: ")
                    msg = input("Write the message: ")
                  
                    send_email(subject, config3.father_email, msg)

                elif "file explorer"in q or "file" in q:
                    codePath = "C:\\Users\\DELL"
                    os.startfile(codePath)
                    speak("opening File Explorer")


                elif "zoom" in q:
                    codePath = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Zoom\\Zoom.lnk"
                    os.startfile(codePath)
                    speak("opening Zoom")

                elif "my google" in q:
                    codePath = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
                    os.startfile(codePath)
                    speak("opening Vayun's Chrome")
                    
                elif "open my c++ app" in q:
                    codePathd = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Bloodshed Dev-C++\Dev-C++.lnk"
                    os.startfile(codePath)
                    speak("Opening Dev C++")

    # root = Tk()
    # root.geometry("170x110")
    # root.title("Jarvis Control Pannel")
    # Switch_On = Button(root,text = "ON",width = 10,command = On, background="Green").place(x =50,y=70)
    # root.mainloop()