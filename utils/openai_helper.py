import os
import tempfile
import uuid

import openai
from dotenv import load_dotenv, find_dotenv
import requests
import soundfile as sf
openai.api_key = os.getenv("OPENAI_API_KEY")

load_dotenv(find_dotenv())

def chat_completion(prompt: str) -> str:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful banking assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message['content']


def transcript_audio(media_url: str) -> dict:
    try:
        ogg_file_path = f'{tempfile.gettempdir()}/{uuid.uuid1()}.aac'
        data = requests.get(media_url)
        with open(ogg_file_path, 'wb') as file:
            file.write(data.content)
        audio_data, sample_rate = sf.read(ogg_file_path)
        mp3_file_path = f'{tempfile.gettempdir()}/{uuid.uuid1()}.mp3'
        sf.write(mp3_file_path, audio_data, sample_rate)
        audio_file = open(mp3_file_path, 'rb')
        os.unlink(ogg_file_path)
        os.unlink(mp3_file_path)
        transcript = openai.Audio.transcribe(
            'whisper-1', audio_file, api_key=os.getenv('OPENAI_API_KEY'))
        return transcript['text']
    except Exception as e:
        print('Error at transcript_audio...')
        print(e)
        return 'Error at transcript_audio...'


if __name__=="__main__":
    # sf.read(r'C:/Users/Dell/AppData/Local/Temp/609d8a53-70c5-11ee-a61d-9061ae1395f1.ogg')
    pass