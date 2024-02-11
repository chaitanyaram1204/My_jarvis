import speech_recognition as sr
#index = 0
'''for name in sr.Microphone.list_microphone_names():
    print(index,' ' ,name)
    index+=1'''
recognizer = sr.Recognizer()
def mic_to_text_class():
    with sr.Microphone(device_index = 0) as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("Recognizing....") 
    try:
        print("You said :",recognizer.recognize_google(audio))
    except:
        pass
    return recognizer.recognize_google(audio)
if __name__ == "__main__":
    mic_to_text_class()