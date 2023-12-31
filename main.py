# imports
import requests
import config
from send_email import send_email

# api key
api_key = config.api_key

# example of url
url = config.url

# make request
request = requests.get(url)

# get a dictionary with data
content = request.json()

# access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news " + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"
        
# encoding method
body = body.encode("utf-8")
send_email(message=body)