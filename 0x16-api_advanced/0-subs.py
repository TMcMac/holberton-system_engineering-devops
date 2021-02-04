#!/usr/bin/python3
"""
A simple script to query a given subreddit
and return total subscribers or 0 if invalid
"""

import json
import requests


def number_of_subscribers(subreddit):
    """Looks up numbers of subscribers to a subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    pull = requests.get(url,
                        headers={"user-agent": "user"},
                        allow_redirects=False).json()
    check = list(pull.keys())
    if 'data' in check:
        subs = pull.get('data').get('subscribers')
    else:
        subs = 0
    return subs
