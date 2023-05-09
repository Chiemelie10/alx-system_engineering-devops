#!/usr/bin/python3
"""This module describes the function 'def top_ten(subreddit)'"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the title of the first 10
    hot posts listed for a given subreddit.
    """

    needed_info = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                               .format(subreddit),
                               headers={"User-Agent": "My-User-Agent"},
                               allow_redirects=False)
    if needed_info.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in needed_info.json().get("data").get("children")]
