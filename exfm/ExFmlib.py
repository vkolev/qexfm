from exfm.ResultList import ResultList

import requests
import urllib2

API_URL = "http://ex.fm/api/v3/"
API_URL_TREND = r"http://ex.fm/api/v3/trending/tag/{tag}"
API_URL_SEARCH = r"http://ex.fm/api/v3/song/search/{term}"


class ExFmLib:

    def __init__(self):
        self.test = 0
        
    def get_trending(self, tag="hip-hop", start=0, end=20):
        url = API_URL_TREND.format(tag=tag)
        payload = {'start': start, 'end': end}
        print url
        r = requests.get(url, params=payload)
        print r.text
        return ResultList(r.text)
    
    def get_search(self, term="", start=0, end=20):
        term = urllib2.quote(term.encode('utf-8'))
        url = API_URL_SEARCH.format(term=term)
        payload = {'start': start, 'end':end}
        r = requests.get(url, params=payload)
        return ResultList(r.text)
        
