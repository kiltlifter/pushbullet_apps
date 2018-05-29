# -*- coding: utf-8 -*-
"""
Module Docstring
"""

from .session import DefaultSession

__author__ = "Sean Douglas"
__version__ = "0.1.0"
__license__ = "MIT"


class HackerNews(DefaultSession):
    def __init__(self):
        super(HackerNews, self).__init__()
        self.base_url = 'https://news.ycombinator.com'

    def current_entries(self, count: int=5):
        r = self.get(self.base_url)
        items = r.html.find('table.itemlist tr td.title > a.storylink')
        items = items[:count]
        return list(tuple([a.text, a.attrs.get('href')]) for a in items)
