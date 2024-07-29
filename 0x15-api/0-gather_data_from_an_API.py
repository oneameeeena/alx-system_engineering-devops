#!/usr/bin/python3
'''
gather user posts data from API
'''

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            user_id = int(sys.argv[1])
            user_req = requests.get('{}/users/{}'.format(REST_API, user_id)).json()
            posts_req = requests.get('{}/posts'.format(REST_API)).json()
            user_name = user_req.get('name')
            user_posts = list(filter(lambda x: x.get('userId') == user_id, posts_req))
            
            print('User {} has made the following posts ({}):'.format(user_name, len(user_posts)))
            if len(user_posts) > 0:
                for post in user_posts:
                    print('\nTitle: {}\nBody: {}\n'.format(post.get('title'), post.get('body')))

