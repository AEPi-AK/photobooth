import os
import json
import urllib
import facepy
import logging
import coloredlogs

logger = logging.getLogger('photobooth')
coloredlogs.install(level=logging.DEBUG)

if os.uname()[4][:3] == 'arm':
    logging.warning("ARM archiecture detected; setting up picamera...")
    import picamera
    camera = picamera.PiCamera()
else:
    logging.warning("Non-ARM archiecture detected; skipping picamera setup")

with open('config.json') as config_file:
    logging.info("Parsing config file..."),
    config = json.load(config_file)
    page_id = config['page_id']
    access_token = config['extended_access_token']

logging.info("Initializing Graph API client...")
graph = facepy.GraphAPI(access_token)

print graph.get('me')
# path = "%s/photos" % page_id
# r = graph.post(path, source=open("test.jpg"))
# print r

# while True:
#     IMG_NAME = "snap.png"
#     raw_input("HIT ME")
#     camera.capture(IMG_NAME)
#     r = graph.post(path, source=open(IMG_NAME))
#     print r
