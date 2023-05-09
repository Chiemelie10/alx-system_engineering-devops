#!/usr/bin/python3
"""This module describes the function 'def number_of_subscribers(subreddit)'"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """

    num_of_subscribers = requests.get("https://www.reddit.com/r/{}/about.json"
                                      .format(subreddit),
                                      headers={"User-Agent": "My-User-Agent"},
                                      allow_redirects=False)
    if number_of_subscribers.status_code >= 300:
        return 0
    return number_of_subscribers.json().get("data").get("subscribers")
