import youtube_dl


def banner():
    print(r"""

  __     __         _         _                     __  __ _____ ____             _____  _
  \ \   / /        | |       | |                   |  \/  |  __ \___ \           |  __ \| |
   \ \_/ /__  _   _| |_ _   _| |__   ___   ______  | \  / | |__) |__) |  ______  | |  | | |
    \   / _ \| | | | __| | | | '_ \ / _ \ |______| | |\/| |  ___/|__ <  |______| | |  | | |
     | | (_) | |_| | |_| |_| | |_) |  __/          | |  | | |    ___) |          | |__| | |____
     |_|\___/ \__,_|\__|\__,_|_.__/ \___|          |_|  |_|_|   |____/           |_____/|______|



""")


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
    banner()
    mp3()
