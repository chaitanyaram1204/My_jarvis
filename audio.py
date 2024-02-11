import speech_recognition as sr

recognizer = sr.Recognizer()

from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

def text_audio(text):
    language = 'en'
    tts = gTTS(text= text, lang=language)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    song = AudioSegment.from_file(fp, format = "mp3")
    play(song)

if __name__ == "__main__":
    text_audio("Hello, I am Jarvis. How can I help you?")   