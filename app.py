from video_sum import download_audio, transcribe_audio, Text_summarize

def main():
    url = input(" Nhập URL video YouTube: ").strip()
    audio_file = "video.mp3"

    download_audio(url, audio_file)
    transcript = transcribe_audio(audio_file)

    print("transcript:")
    print(transcript)

    summary = Text_summarize(transcript)

    print("\n summarize:")
    print(summary)

    with open("summary.md", "w", encoding="utf-8") as f:
        f.write(summary)
        print("\n Đã lưu vào summary.md")

if __name__ == "__main__":
    main()
