import subprocess
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--mute-audio")
options.headless = True # Prevents browsers from being opened by Selenium

def get_playlists(genre : str, scrolls : int):
    """
    Gets a list of links for playlists that are on soundcloud.

    TODO: Add arg to allow choice of how many playlists you want or how many songs total you'd like
    TODO: Add additional search options

    :param genre: Genre of music that you want to get playlist links for.
    :param scrolls: Amount of times you'd like to scroll down to load more playlists
    :return: List of links to playlists
    """
    browser = webdriver.Chrome("chromedriver.exe", options=options)
    url = "https://soundcloud.com/search/sets?q=%23" + genre + "&filter.genre_or_tag=" + genre
    browser.get(url)
    time.sleep(2) # Won't work unless we give time to let page load
    body = browser.find_element_by_tag_name("body")
    for i in range(scrolls): # Scrolling page to let more playlists load on page before getting HTML
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
    time.sleep(2) 
    soup = BeautifulSoup(browser.page_source, 'lxml')
    div = soup.find("div", {"class": "l-main"})
    playlists = div.findAll("a", {"class": "soundTitle__title sc-link-dark"})
    playlist_links = []
    for p in playlists:
        playlist_links.append("https://soundcloud.com" + p["href"])

    return playlist_links

def get_songs(playlist_links : list, scrolls : int):
    """
    Get the links of individual songs belonging to the playlists.

    TODO: Handle case where there may be duplicates of songs (i.e. song belonging to multiple playlists). Maybe handle
          after scraping tho?
    TODO: Automate the number of times function needs to scroll to load all songs in a playlist

    :param links: List of links to soundcloud playlists.
    :param scrolls: Number of times you'd like to scroll in a playlist to load more songs
    :return: List of links to songs.
    """
    song_links = []
    for url in playlist_links:
        browser = webdriver.Chrome("chromedriver.exe", options=options)
        browser.get(url)
        body = browser.find_element_by_tag_name("body")

        for i in range(scrolls):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
        time.sleep(2)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        div = soup.find("div", {"class": "listenDetails"})
        songs = div.findAll("a", {"class": "trackItem__trackTitle sc-link-dark sc-font-light"})
        for s in songs:
            song_links.append("https://soundcloud.com" + s["href"])

    return song_links

def download(url : str):
    test = subprocess.run(["./youtubedl/youtube-dl.exe", url, "-o %(title)s.%(ext)s"])

if __name__ == "__main__":
    playlists = get_playlists("pop", 10)
    print(len(get_songs(playlists, 10)))
    # download("https://soundcloud.com/oliviarodrigo/drivers-license?in=soundcloud-shine/sets/ear-candy-fresh-pop-picks")

