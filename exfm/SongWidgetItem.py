'''
Created on May 5, 2013

@author: vladi
'''
from PyQt4 import QtGui


class SongWidgetItem(QtGui.QListWidgetItem):
    
    def __init__(self, song, icon):
        super(SongWidgetItem, self).__init__()
        self.song = song
        self.setIcon(icon)
        self.setText(song.artist + " - " + song.title)
        
    def get_song(self):
        return self.song