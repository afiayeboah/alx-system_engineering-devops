#!/usr/bin/python3
'''
    This module provides a function to retrieve the top ten posts
    for a given subreddit.
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        Retrieve the top ten posts for a specified subreddit.
    '''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Safari/537.36'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            for i in range(10):
                print(data['data']['children'][i]['data']['title'])
        else:
            print("Error: Unable to retrieve top ten posts")
    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred during the request - {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 filename.py <subreddit>")
    else:
        subreddit_name = argv[1]
        top_ten(subreddit_name)
