#!/usr/bin/python3
"""Module for task"""

import requests


def number_of_subscribers(subreddit):
    """a function that queries the Reddit API
and returns the number of subscribers """

    retrived = requests.get("https:/www.reddit.com/r/{}/about.json".
                            format(subreddit),
                            headers={"User-Agent": "KIDIST-123"})
    if retrived.status_code != 200:
        return 0
    else:
        return retrived.json().get("data").get("subscribers")
