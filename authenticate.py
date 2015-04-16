# Okay, so you want to generate the long-lived token that enables
# photobooth to post to the Facebook page (as one of its admins).

# Step 1: Generate the confirmation dialog URL
import urllib
import json

with open('config.json') as config_file:
    config = json.load(config_file)

url = "https://www.facebook.com/dialog/oauth?"
url += urllib.urlencode({
    "response_type": "token",
    'client_id': config['app_id'],
    'redirect_uri': "https://www.facebook.com/connect/login_success.html",
    "scope": ",".join(["publish_actions", "manage_pages"])
})

print url

# Step 2: quickly (before you get redirected to "SECURITY WARNING"
# copypaste the value of ACCESS_TOKEN
# which you'll get as a URL hash/fragment at the end of step 1.

# Looks something like:

# https://www.facebook.com/connect/login_success.html#access_token=<token>&expires_in=5183427

# Step 3: Paste the extended access token into config.json!
