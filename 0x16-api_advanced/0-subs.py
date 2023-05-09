#!/usr/bin/python3
"""
Queries the Reddit API module
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": 'My Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        num_subs = data.get("data").get("subscribers")
        return num_subs
    else:
        return 0
