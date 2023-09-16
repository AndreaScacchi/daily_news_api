# imports
import requests
import config

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
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"
        
body = body.encode("utf-8")
send_email(message=body)