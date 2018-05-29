# -*- coding: utf-8 -*-
"""
Module Docstring
"""

import argparse
import json
import os
from datetime import datetime
from .meh import Meh
from .hacker_news import HackerNews
from .pushbullet import Pushbullet

__author__ = "Sean Douglas"
__version__ = "0.1.0"
__license__ = "MIT"

CONFIG = os.path.join(os.path.dirname(__file__), os.pardir, 'config.json')


def meh():
    m = Meh()
    data = m.deal_today()
    if args.print:
        print(data)
    else:
        p = Pushbullet(api_key=config['API']['pushbullet']['key'])
        p.send_link(title=data['title'] + ' ' + data['price'], url=data['link'])


def hacker_news():
    n = HackerNews()
    data = n.current_entries(count=args.count if args.count else None)
    if args.print:
        print(data)
    else:
        p = Pushbullet(api_key=config['API']['pushbullet']['key'])
        p.send_note(title='Hacker News {}'.format(datetime.now().strftime('%m/%d')),
                    body='\n'.join(['{}: {}'.format(a[0], a[1]) for a in data]))



if __name__ == "__main__":
    with open(CONFIG, 'r') as f:
        config = json.load(f)

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(help='sub-command help.', dest='command')

    encoding_parser = subparser.add_parser('meh', help='Push daily deal from meh')
    encoding_parser.add_argument('-p', '--print', action='store_true', help='Print to console only')

    encoding_parser = subparser.add_parser('hacker_news', help='Current articles from hacker news')
    encoding_parser.add_argument('-c', '--count', type=int, help='Number of news stories to return')
    encoding_parser.add_argument('-p', '--print', action='store_true', help='Print to console only')

    args = parser.parse_args()

    if args.command == 'meh':
        meh()
        exit(0)
    elif args.command == 'hacker_news':
        hacker_news()
        exit(0)
    else:
        parser.print_help()
