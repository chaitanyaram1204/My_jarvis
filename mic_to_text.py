import speech_recognition as sr
index = 0
for name in sr.Microphone.list_microphone_names():
    print(index,' ' ,name)
    index+=1