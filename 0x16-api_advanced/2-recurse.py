#!/usr/bin/python3
"""A function to recursively retrieve titles of hot posts on a subreddit."""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively retrieves titles of hot posts on a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit.
    hot_list (list): A list to store the titles of hot posts.
    after (str): A parameter indicating the page to start retrieving from.
    count (int): A count of the number of posts retrieved.

    Returns:
    list: A list containing titles of hot posts on the subreddit.
    If the subreddit doesn't exist or if there's an error, it returns None.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:
                       v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
