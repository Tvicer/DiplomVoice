import speech_recognition as sr
from pydub import AudioSegment

# Инициализируем распознаватель речи
r = sr.Recognizer()


# Функция для распознавания речи из аудио файла
def transcribe_audio(audio_file):
    sound = AudioSegment.from_file(audio_file, format="webm")  # Загружаем MP3 файл
    wav_file = "temp.wav"  # Временный WAV файл
    sound.export(wav_file, format="wav")  # Конвертируем MP3 в WAV

    with sr.AudioFile(wav_file) as source:
        audio_data = r.record(source)  # читаем аудио файл
        duration = source.DURATION  # получаем длительность аудио

    try:
        text = r.recognize_google(audio_data, language='ru-RU')  # распознаем текст на русском языке
        return text, duration
    except sr.UnknownValueError:
        print("Распознаватель речи не смог обработать аудио")
        return None, None  # Возвращаем None для текста и длительности
    except sr.RequestError as e:
        print(f"Ошибка сервиса распознавания речи: {e}")
        return None, None  # Возвращаем None для текста и длительности

# Список аудио файлов для обработки
audio_files = ['c1.webm']



# Перебираем аудио файлы и добавляем данные в словарь
for audio_file in audio_files:
    text, duration = transcribe_audio(audio_file)
    if text is not None:  # Проверяем, что текст не равен None
        print(f"Распознанный текст: {text}")
        print(f"Длительность аудио: {duration} секунд")

