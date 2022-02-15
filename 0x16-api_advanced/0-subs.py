#!/usr/bin/python3
"""Module for task"""

import requests
def number_of_subscribers(subreddit):
    """a function that queries the Reddit API and returns the number of subscribers """

    retrived = requests.get("https:/www.reddit.com/r/{}/about.json".
                           format(subreddit),allow_redirects=False)
    if retrived.status_code is not 200:
        return 0
    else:
        return retrived.json().get("data").get("subscribers")
    
