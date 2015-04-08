import json
from facepy import GraphAPI
import picamera

with open('config.json') as config_file:
    config = json.load(config_file)
    album_id = config['album_id']
    page_id = config['page_id']
    access_token = config['access_token']

camera = picamera.PiCamera()
graph = GraphAPI(access_token)
# album = graph.get_object(album_id)
# print album

path = "%s/photos" % page_id

while True:
    IMG_NAME = "snap.png"
    raw_input("HIT ME")
    camera.capture(IMG_NAME)
    r = graph.post(path, source=open(IMG_NAME))
    print r
