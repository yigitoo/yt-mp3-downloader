from yt_dlp import YoutubeDL
import os

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def get_url_list_from_file() -> list[str]:
    with open('urls.txt', 'r') as f:
        urls = f.read().splitlines()
    return urls

def download_mp3():
    with YoutubeDL(ydl_opts) as ydl:
        filenames: list[str] = get_url_list_from_file()
        print(ydl.download(filenames))

def save_url_to_file(filename: str) -> None:
    with open('urls.txt', 'a') as f:
        f.write(filename + '\n')


def reset_url_text_file() -> None:
    with open('urls.txt', 'w') as f:
        f.write("")

def install_music_from_youtube() -> None:
    reset_url_text_file()
    print('Youtube MP3 Downloader\n')
    print('If you want to stop download list')
    while True:
        url: str = input("Enter url: ")

        if url == '':
            break

        save_url_to_file(url)

    os.system('yt-dlp --rm-cache')
    download_mp3()


    os.makedirs('musics', exist_ok=True)
    if os.name == 'nt':
        os.system('move *.mp3 musics')
    else:
        os.system('mv *.mp3 musics')


if __name__ == "__main__":
    is_single = input('Download mode single / whole playlist (s-single/p-playlist): ')

    if is_single.lower() in ['s', 'single']:
        ydl_opts['noplaylist'] = True
        install_music_from_youtube()
    elif is_single.lower() in ['p', 'playlist']:
        ydl_opts['noplaylist'] = False
        install_music_from_youtube()
    else:
        print('Mode cannot detected. Exiting...')
