'''
Created on May 5, 2013

@author: vladi
'''
import requests
from PyQt4.QtGui import QPixmap
from PyQt4.QtCore import Qt


class Image(object):
    
    def __init__(self, image=None):
        self.small = ""
        self.medium = ""
        self.large = ""
        if image != None:
            self.small = image['small']
            self.large = image['large']
            self.medium = image['medium']
            
    def get_small_pixmap(self):
        pm = QPixmap()
        if self.small is not "":
            r = requests.get(self.small)
            pm.loadFromData(r.content, None)
        return pm.scaled(32, 32, Qt.IgnoreAspectRatio)