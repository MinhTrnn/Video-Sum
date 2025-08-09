import os
import subprocess
from openai import OpenAI
import whisper


def download_audio(url, output_path='video.mp3'):
    command = f'yt-dlp -x --audio-format mp3 -o "{output_path}" {url}'
    subprocess.run(command, shell=True)


def transcribe_audio(file_path):
    model = whisper.load_model("base")

    result = model.transcribe(audio=file_path, language=None, fp16=False)

    return result["text"]


def Text_summarize(text):

    client = OpenAI(
        api_key='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',
        base_url='https://openrouter.ai/api/v1',
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """You are a developer. Your task is to analyze the transcript of a YouTube video provided by the user.

You are working with your colleagues. First, you must extract and present the full original English script from the transcript, exactly as spoken.

Then, translate the entire script into Vietnamese.


"""
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content
