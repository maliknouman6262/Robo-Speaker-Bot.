import pyttsx3

if __name__ == "__main__":
    engine = pyttsx3.init()
    
    print("Welcome to Robo-Speaker 1.1.0 created by Malik Nouman")
    while True:
        user_input = input("Enter the text you want to speak (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            engine.say("say'bye bye friend'")
            print("Goodbye!")
            break
        engine.say(user_input)
        engine.runAndWait()
