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
from .steep_and_cheap import SteepAndCheap

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


def steep_and_cheap():
    s = SteepAndCheap(config['Steep and Cheap']['keywords'], config['Steep and Cheap']['exclusions'])
    r = s.execute()
    if r and args.print:
        [print(a) for a in r]
        exit(0)
    elif r:
        p = Pushbullet(api_key=config['API']['pushbullet']['key'])
        content = []
        for m in r:
            info = 'Current' if not m['upcoming'] else f'@{m["upcoming"]}'
            content.append(dict(
                title=info + ': ' + m['title'] + ' - ' + m['price'],
                url=m['link']
            ))
        p.send_note(title=f'Steep and Cheap: {datetime.now().strftime("%m/%d %H:%M")}',
                    body='\n'.join([f'{i["title"]}: https://www.steepandcheap.com{i["url"]}' for i in content]))




if __name__ == "__main__":
    with open(CONFIG, 'r') as f:
        config = json.load(f)

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(help='sub-command help.', dest='command')

    meh_parser = subparser.add_parser('meh', help='Push daily deal from meh')
    meh_parser.add_argument('-p', '--print', action='store_true', help='Print to console only')

    hn_parser = subparser.add_parser('hacker_news', help='Current articles from hacker news')
    hn_parser.add_argument('-c', '--count', type=int, help='Number of news stories to return')
    hn_parser.add_argument('-p', '--print', action='store_true', help='Print to console only')

    snc_parser = subparser.add_parser('steep_and_cheap', help='Push current steep and cheap deals matching criteria')
    snc_parser.add_argument('-p', '--print', action='store_true', help='Print to console only')

    args = parser.parse_args()

    if args.command == 'meh':
        meh()
        exit(0)
    elif args.command == 'hacker_news':
        hacker_news()
        exit(0)
    elif args.command == 'steep_and_cheap':
        steep_and_cheap()
        exit(0)
    else:
        parser.print_help()
