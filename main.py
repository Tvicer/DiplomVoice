import speech_recognition as sr
from pydub import AudioSegment
from flask import Flask, request
import os

app = Flask(__name__)
r = sr.Recognizer()

@app.route('/api/voiceToText/send', methods=['POST'])
def index():
    json = request.get_json()

    audio_files = ['C:/Users/Tvicer/Downloads/' + json["voice"]]

    for audio_file in audio_files:
        text, duration = transcribe_audio(audio_file)
        os.remove('C:/Users/Tvicer/Downloads/' + json["voice"])
        return text

def transcribe_audio(audio_file):
    sound = AudioSegment.from_file(audio_file, format="webm")
    wav_file = "temp.wav"
    sound.export(wav_file, format="wav")

    with sr.AudioFile(wav_file) as source:
        audio_data = r.record(source)
        duration = source.DURATION

    try:
        text = r.recognize_google(audio_data, language='ru-RU')
        return text, duration
    except sr.UnknownValueError:
        print("Распознаватель речи не смог обработать аудио")
        return None, None
    except sr.RequestError as e:
        print(f"Ошибка сервиса распознавания речи: {e}")
        return None, None


if __name__ == "__main__":
    app.run(debug=False)