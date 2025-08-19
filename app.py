from video_sum import download_audio, transcript_audio, text_summarize, save_text
import os

def main():
    url = input('url:').strip()
    downloaded = download_audio(url)
    transcripted = transcript_audio(downloaded)
    save_text(os.path.join(os.getcwd(), "transcript.txt"), transcripted)
    summary = text_summarize(transcripted)
    save_text(os.path.join(os.getcwd(), "summary.txt"), summary)
    print(summary)

if __name__ == '__main__':
    main()
