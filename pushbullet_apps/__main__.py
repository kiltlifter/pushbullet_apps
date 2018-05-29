# -*- coding: utf-8 -*-
"""
Module Docstring
"""

import argparse
import json
import os
from .meh import Meh
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



if __name__ == "__main__":
    with open(CONFIG, 'r') as f:
        config = json.load(f)

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(help='sub-command help.', dest='command')

    encoding_parser = subparser.add_parser('meh', help='Push daily deal from meh')
    encoding_parser.add_argument('-p', '--print', action='store_true', help='Print to console only')

    args = parser.parse_args()

    if args.command == 'meh':
        meh()
        exit(0)
    else:
        parser.print_help()
