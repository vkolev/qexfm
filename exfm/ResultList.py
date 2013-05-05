'''
Created on May 5, 2013

@author: vladi
'''
from exfm.Song import Song
from exfm.Image import Image
import json


class ResultList:
    
    def __init__(self, json_data):
        self.songs = self.__get_songs(json_data)
        
    def __get_songs(self, json_data):
        songs = []
        data = json.loads(json_data)
        for item in data['songs']:
            song = Song()
            song.artist_twitter = item['artist_twitter']
            song.album = item['album']
            song.edit_id = item['edit_id']
            song.buy_link = item['buy_link']
            song.image = Image(item['image'])
            song.similar_artists = item['similar_artists']
            song.last_loved = item['last_loved']
            song.artist = item['artist']
            song.title = item['title']
            song.url = item['url']
            songs.append(song)
        return songs
            
        