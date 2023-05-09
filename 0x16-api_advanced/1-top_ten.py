#!/usr/bin/python3
"""
Reddit API Module
"""

import requests


def top_ten(subreddit):
    """
    Queries Reddit API and prints titles of the first 10 hot posts listed
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": 'My agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()

        for post in posts['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
