#!/usr/bin/python3
"""
Reddit API query module
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    recursive function that queries the Reddit API and returns a list
    """
    headers = {'User-agent': 'my agent'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=50&after={}".format(
            subreddit, after)
    posts = requests.get(url, headers=headers, allow_redirects=False)

    if posts.status_code == 200:
        posts = posts.json()['data']
        after = posts['after']
        posts = posts['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        if after is not None:
            recurse(subreddit, hot_list, after)
        return (hot_list)
    else:
        return (None)
