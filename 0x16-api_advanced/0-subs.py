#!/usr/bin/python3
'''
    This module provides a function to retrieve the number of subscribers
    for a given subreddit.
'''

import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
        Retrieve the number of subscribers for a specified subreddit.
    '''
    user_agent = {'User-Agent': 'Lizzie'}

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    response = requests.get(url, headers=user_agent)

    if response.status_code == 200:

        data = response.json()

        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
    else:

        return 0


if __name__ == "__main__":
    subreddit_name = argv[1]

    print(number_of_subscribers(subreddit_name))
