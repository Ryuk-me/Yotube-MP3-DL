import youtube_dl


def mp3():
    video_link = input("Enter Video Link :")
    video_info = youtube_dl.YoutubeDL().extract_info(url=video_link, download=False)

    fileName = f"{video_info['title']}.mp3"
    option = {
        'format': 'bestaudio/best',
        'outtmpl': fileName,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(option) as yt:
        yt.download([video_info['webpage_url']])



if __name__ == "__main__":
    mp3()
