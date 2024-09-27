# 0-subs.py
"""
Uses Reddit API to print the number of subscribers of a subreddit
"""
import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyBot/0.1'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("Error: Request to Reddit API failed.")
        return 0

    data = response.json().get("data")
    num_subs = data.get("subscribers")

    print("Number of Subscribers:", num_subs)

    return num_subs
