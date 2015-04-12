# Okay, so you want to generate the long-lived token that enables
# photobooth to post to the Facebook page (as one of its admins).

# Step 1: Generate the confirmation dialog URL
import urllib

url = "https://www.facebook.com/dialog/oauth?"
url += urllib.urlencode({
    "response_type": "token",
    'client_id': config['app_id'],
    'redirect_uri': "https://www.facebook.com/connect/login_success.html",
    "scopes": ",".join(["publish_actions", "manage_pages"])
})

print urllib

# Step 2: quickly (before you get redirected to "SECURITY WARNING"
# copy-and-paste the value of ACCESS_TOKEN
# which you'll get as a URL hash/fragment at the end of step 1.

# Looks something like:

https://www.facebook.com/connect/login_success.html#access_token=<token>&expires_in=5183427

# Step 3: Exchange short-lived token for extended access token

token = facepy.utils.get_extended_access_token(
    "<TOKEN GOES HERE>",
    config['app_id'],
    config['app_secret']
)

print token

# Step 4: Copy and paste the extended access token into config.json!
