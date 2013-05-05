'''
Created on May 5, 2013

@author: vladi
'''

class Image(object):
    
    def __init__(self, image=None):
        self.small = ""
        self.medium = ""
        self.large = ""
        if image != None:
            self.small = image['small']
            self.large = image['large']
            self.medium = image['medium']