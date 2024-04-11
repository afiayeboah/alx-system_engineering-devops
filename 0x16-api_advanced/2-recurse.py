#!/usr/bin/python3
"""
Using reddit's API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returning top ten post titles recursively"""
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'after': after} if after else {}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        data = results.json().get("data")
        after_data = data.get("after")

        if after_data:
            hot_list = recurse(subreddit, hot_list, after=after_data)

        all_titles = data.get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))

        return hot_list
    else:
        return None
