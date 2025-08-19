import os
import subprocess
from dotenv import load_dotenv
from openai import OpenAI
import datetime

load_dotenv()
api = os.getenv('API_KEY')
url = os.getenv('URL')

def download_audio(url: str) -> str:
    dt = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
    file_name = f"{dt}.mp3"
    save_dir = os.getcwd()
    file_path = os.path.join(save_dir, file_name)
    command = f'yt-dlp -x --audio-format mp3 -o "{file_path}" {url}'
    subprocess.run(command, shell=True)
    return file_path

def transcript_audio(file_path: str) -> str:
    client = OpenAI(api_key=api, base_url=url)
    with open(file_path, 'rb') as audio_file:
        transcript = client.audio.transcriptions.create(
            model='gpt-4o-transcribe',
            file=audio_file
        )
    return transcript.text

def text_summarize(text: str) -> str:
    client = OpenAI(api_key=api, base_url=url)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": """You are a developer. Your task is to analyze the transcript of a YouTube video provided by the user.

You are working with your colleagues.You must extract the script and translate it to Vietnamese. After that, summarize.



"""
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )
    return response.choices[0].message.content

def save_text(file_path: str, text: str) -> None:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
