from requests import get
from bs4 import BeautifulSoup
import json
import time

important_features = ["permalink_url", "genre", "id"]


def scrape_range(start: int, stop: int, client_id: str):
    global important_features
    text = get(
        f"https://api-v2.soundcloud.com/tracks?ids={','.join(str(i) for i in range(start, stop))}&client_id={client_id}"
    ).text
    return [
        {key: song[key] for key in (song.keys() & important_features)}
        for song in json.loads(text)
    ]


def main():
    step = 16
    songs = []
    i = 0
    for i in range(256, 512, step):
        songs.extend(scrape_range(i, i + step, "3DLVBKZxoYMm5gFm9YjFxJTNFL0VECz7"))
    print(songs)


if __name__ == "__main__":
    main()
