# -*- coding: utf-8 -*-
"""
Module Docstring
"""

from .session import DefaultSession
import re
from datetime import timedelta
from dateutil.parser import parse


__author__ = "Sean Douglas"
__version__ = "0.1.0"
__license__ = "MIT"


class SteepAndCheap(DefaultSession):
    def __init__(self, keywords: list, exclusions: list):
        super(SteepAndCheap, self).__init__()
        self.base_url = 'https://www.steepandcheap.com'
        self.keywords = keywords
        self.exclusions = exclusions

    def get_deal(self):
        r = self.get(self.base_url + '/data/odat.json')
        if not r.ok:
            print(f'Bad status code: {r.status_code}')
        else:
            return r.json()

    def approx_time(self, next_deal_t_stamp: str, index: int):
        date = parse(next_deal_t_stamp)
        date = date + timedelta(minutes=5*index)
        date = date + timedelta(hours=-7)
        return f'{date.hour}:{date.minute}'

    def search_titles(self, content: dict):
        matches = []
        for phrase in self.keywords:
            p = re.compile(phrase, re.IGNORECASE)
            t = content.get('productTitle')
            if t and p.search(t.lower()):
                matches.append({
                    'title': f'{content["productTitle"]}',
                    'price': f'{content["salePrice"]}',
                    'link': f'{content["url"]}',
                    'upcoming': False
                })
            for idx, u in enumerate(content.get('upcoming')):
                t = u.get('productTitle')
                if t and p.search(t.lower()):
                    matches.append({
                        'title': f'{u["productTitle"]}',
                        'price': f'{u["salePrice"]}',
                        'link': f'{u["url"]}',
                        'upcoming': self.approx_time(content.get('nextUpdateString'), idx)
                    })

        for m in matches:
            for e in self.exclusions:
                z = re.search(str(e), m['title'], flags=re.IGNORECASE)
                if z:
                    matches.remove(m)
                break

        return matches

    def execute(self):
        d = self.get_deal()
        return self.search_titles(d)

