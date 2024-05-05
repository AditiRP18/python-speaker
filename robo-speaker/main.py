import pyttsx3

if __name__ == '__main__':
    print("Welcome to Robo-Speaker!")
    while True:
        x=input("Enter what you want me to speak: ")
        if(x=="q"):
            engine = pyttsx3.init()
            engine.say("GoodBye")
            engine.runAndWait()
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()