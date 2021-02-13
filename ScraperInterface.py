class ScraperInterface:

    def get_playlists(self, genre : str, scrolls : int):
        """Get playlists containing songs of a particular genre"""
        pass

    def get_songs(self, playlist_links: list, scrolls: int) -> list:
        """Get song urls from list of songs given in the playlists"""
        pass

    def get_tags(self):
        """Get tags belonging to individual songs"""
        pass