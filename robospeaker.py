import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        # Get the user's input
        text = input("Enter what you want me to speak: ")

        # Process the user's input
        if text == "q":
            break
        else:
            # Speak the user's input
            speak(text)
