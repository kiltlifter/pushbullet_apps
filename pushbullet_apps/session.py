# -*- coding: utf-8 -*-
"""
Default session used to make requests
"""

from requests_html import HTMLSession

__author__ = "Sean Douglas"
__version__ = "0.1.0"
__license__ = "MIT"


class DefaultSession(HTMLSession):
    def __init__(self):
        super(DefaultSession, self).__init__()
        self.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                                     'Chrome/66.0.3359.139 Safari/537.36'
