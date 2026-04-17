import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use microphone as source
with sr.Microphone() as source:
    print("Speak something...")
    
    # Adjust for noise
    recognizer.adjust_for_ambient_noise(source)
    
    # Listen
    audio = recognizer.listen(source)

try:
    # Convert speech to text
    text = recognizer.recognize_google(audio)
    print("You said:", text)

except sr.UnknownValueError:
    print("Sorry, could not understand audio")

except sr.RequestError:
    print("Could not request results from service")