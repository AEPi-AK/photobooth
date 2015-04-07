import json
from facepy import GraphAPI
import requests

with open('config.json') as config_file:
    config = json.load(config_file)
    album_id = config['album_id']
    page_id = config['page_id']
    access_token = config['access_token']

graph = GraphAPI(access_token)
# album = graph.get_object(album_id)
# print album

# url = 'http://httpbin.org/post'
# multiple_files = [('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
#                   ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
# r = requests.post(url, files=multiple_files)

path = "%s/photos" % page_id
r = graph.post(path, source=open('test.png'))
print r

# posts = graph.get_connections(profile['id'], 'posts')
#
# while True:
#     try:
#         # Perform some action on each post in the collection we receive from
#         # Facebook.
#         [some_action(post=post) for post in posts['data']]
#         # Attempt to make a request to the next page of data, if it exists.
#         posts = requests.get(posts['paging']['next']).json()
#     except KeyError:
#         # When there are no more pages (['paging']['next']), break from the
#         # loop and end the script.
#         break
