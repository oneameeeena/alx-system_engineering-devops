#!/usr/bin/python3
""" Export user posts to csv """
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    res = requests.get(url_user)
    """Get username"""
    user_name = res.json().get('username')
    posts_url = 'https://jsonplaceholder.typicode.com/posts?userId=' + user
    res = requests.get(posts_url)
    posts = res.json()

    with open('{}_posts.csv'.format(user), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['UserId', 'Username', 'PostId', 'Title', 'Body'])
        for post in posts:
            post_id = post.get('id')
            title = post.get('title')
            body = post.get('body')
            """Write each post to CSV"""
            writer.writerow([user, user_name, post_id, title, body])

