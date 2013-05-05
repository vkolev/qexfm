'''
Created on May 5, 2013

@author: vladi
'''
from exfm.Image import Image

class Song(object):
    
    def __init__(self):
        self.artist_twitter = ""
        self.image = Image()
        self.edit_id = None
        self.sources = []
        self.loved_count = 0
        self.id = ""
        self.album = None
        self.similar_artists = []
        self.title = ""
        self.viewer_love = 0
        self.trending_rank_today = None
        self.buy_link = ""
        self.artist = ""
        self.url = ""
        self.last_loved = ""
        
    def get_url(self):
        if "soundcloud" in self.url:
            self.url += "?consumer_key=leL50hzZ1H8tAdKCLSCnw"
        return self.url
        