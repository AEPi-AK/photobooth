import os
import json
import urllib
import facepy
import logging
import datetime
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
    access_token = config['page_access_token']

logging.info("Initializing Graph API client...")
graph = facepy.GraphAPI(access_token)

path = "%s/photos" % page_id

def takePictureAndUploadIt():
    img_name = "snap-%s.jpg" % datetime.datetime.now().isoformat()
    camera.capture(img_name)
    r = graph.post(path, source=open(img_name))

while True:
    if raw_input("\nTake picture? ['n' to bail] ") == "n": break
    takePictureAndUploadIt()
