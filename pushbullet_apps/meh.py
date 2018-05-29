# -*- coding: utf-8 -*-
"""
Module Docstring
"""

from .session import DefaultSession
import re

__author__ = "Sean Douglas"
__version__ = "0.1.0"
__license__ = "MIT"


class Meh(DefaultSession):
    def __init__(self):
        super(DefaultSession, self).__init__()
        self.base_url = 'https://meh.com'

    def deal_today(self) -> dict:
        r = self.get(self.base_url)
        title = r.html.find('section.features h2', first=True).text
        price = r.html.find('#hero-buttons button', first=True).text
        price = re.sub('\s[bB]uy\s[iI]t\s*', '', price)
        return {'title': title, 'price': price, 'link': self.base_url}

