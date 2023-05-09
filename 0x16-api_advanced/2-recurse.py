#!/usr/bin/python3
"""
This module describes the function 'def recurse(subreddit,
hot_list=[], count=0, after=None)'
"""

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    A recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given
    subreddit. If no results are found for the given subreddit, the
    function should return None.
    """

    needed_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                               .format(subreddit),
                               params={"count": count, "after": after},
                               headers={"User-Agent": "My-User-Agent"},
                               allow_redirects=False)
    if needed_info.status_code >= 400:
        return None

    hot_l = hot_list + [child.get("data").get("title")
                        for child in needed_info.json()
                        .get("data")
                        .get("children")]

    info = needed_info.json()
    if not info.get("data").get("after"):
        return hot_l

    return recurse(subreddit, hot_l, info.get("data").get("count"),
                   info.get("data").get("after"))
