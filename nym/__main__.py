#!/usr/bin/env python3

"""
Nym

Find synonymns and antonymns of common words instantly!

Usage:

nym <word>


Example:

$ nym fun | head -5

amusing
enjoyable
entertaining
lively
pleasant
"""


import sys
import urllib.parse
import requests
import pyquery


if len(sys.argv) != 2:
        print(__doc__)
        exit(0)


try:
        word = urllib.parse.quote(sys.argv[1])
        response = requests.get(f'https://www.thesaurus.com/browse/{word}').text

except Exception as error:
        print(f'Error: {error}')
        exit(0)


document = pyquery.PyQuery(response)
synonymns = document('#meanings [href*="/browse/"]')


for synonymn in synonymns:
        print(synonymn.text)
