import json
import facebook
import requests

with open('config.json') as config_file:
    config = json.load(config_file)

graph = facebook.GraphAPI(config['access_token'])
album = graph.get_object(config['album_id'])
print album

# posts = graph.get_connections(profile['id'], 'posts')

while True:
    try:
        # Perform some action on each post in the collection we receive from
        # Facebook.
        [some_action(post=post) for post in posts['data']]
        # Attempt to make a request to the next page of data, if it exists.
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.
        break
