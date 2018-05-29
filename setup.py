# -*- coding: utf-8 -*-

from distutils.core import setup

__author__ = "Sean Douglas"
__version__ = "0.1.0"
__license__ = "MIT"

setup(
    name='pushbullet_apps',
    version=__version__,
    author='Sean Douglas',
    author_email='seancdouglas@gmail.com',
    packages=['pushbullet_apps'],
    url='https://github.com/kiltlifter/pushbullet_apps',
    license='LICENSE.txt',
    description='Useful ways to distribute information via pushbullet',
    long_description=open('README.md').read(),
    install_requires=[
        'requests-html'
    ],
    python_requires='>=3.6.0'
)

