# -*- coding: utf-8 -*-
"""
Module Docstring
"""

from .session import DefaultSession

__author__ = "Sean Douglas"
__version__ = "0.1.0"
__license__ = "MIT"


class Pushbullet(DefaultSession):
    def __init__(self, api_key: str):
        super(Pushbullet, self).__init__()
        self.base_url = 'https://api.pushbullet.com/v2'
        self.headers['Access-Token'] = api_key
        self.headers['Content-Type'] = 'application/json'

    def send_note(self, title: str=None, body: str=None):
        r = self.post(
            url=self.base_url + '/pushes',
            json={'type': 'note', 'title': title, 'body': body}
        )
        if not r.ok:
            raise r.raise_for_status()

    def send_link(self, title: str=None, body: str=None, url: str=None):
        r = self.post(
            url=self.base_url + '/pushes',
            json={'type': 'link', 'title': title, 'body': body, 'url': url}
        )
        if not r.ok:
            raise r.raise_for_status()

    def send_file(self, body: str=None, file_name: str=None, file_type: str=None, file_url: str=None):
        pass

