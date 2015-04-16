import os
import json
import time
import urllib
import facepy
import logging
import datetime
import coloredlogs

logger = logging.getLogger('photobooth')
coloredlogs.install(level=logging.DEBUG)

if os.uname()[4][:3] == 'arm':
    logging.warning("ARM archiecture detected; setting up picamera & GPIO...")
    IS_PI = True
    import picamera
    import RPi.GPIO as GPIO
    camera = picamera.PiCamera()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
else:
    IS_PI = False
    logging.warning("Non-ARM archiecture detected; skipping picamera & GPIO setup")

with open('config.json') as config_file:
    logging.info("Parsing config file..."),
    config = json.load(config_file)
    page_id = config['page_id']
    access_token = config['page_access_token']

logging.info("Initializing Graph API client...")
graph = facepy.GraphAPI(access_token)

path = "%s/photos" % page_id

def takePictureAndUploadIt():
    time.sleep(0.1) # Rate limiting
    img_name = "snap-%s.jpg" % datetime.datetime.now().isoformat()
    camera.capture(img_name)
    r = graph.post(path, source=open(img_name))

if IS_PI:
    while True:
        input_state = GPIO.input(3)
        if input_state == False:
            logging.debug('Button pressed!!')
            takePictureAndUploadIt()
else:
    while True:
        if raw_input("\nTake picture? ['n' to bail] ") == "n": break
        takePictureAndUploadIt()
