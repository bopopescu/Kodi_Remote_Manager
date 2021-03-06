# -*- coding: UTF-8 -*-


import re

from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import source_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['watchepisodes4.com']
        self.base_link = 'https://www.watchepisodes4.com/'

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            clean_title = cleantitle.geturl(tvshowtitle)
            url = self.base_link + clean_title
            return url
        except:
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if not url:
                return
            r = client.request(url)

            r = re.compile('<a title=".+? Season ' + season + ' Episode ' + episode + ' .+?" href="(.+?)">').findall(r)
            for url in r:
                return url
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []
            hostDict = hostprDict + hostDict
            r = client.request(url)
            r = re.compile('class="watch-button" data-actuallink="(.+?)"').findall(r)
            for url in r:
                valid, host = source_utils.is_host_valid(url, hostDict)
                if valid:
                    sources.append({'source': host, 'quality': 'SD', 'language': 'en', 'url': url, 'direct': False, 'debridonly': False})
        except Exception:
            return

        return sources

    def resolve(self, url):
        return url
