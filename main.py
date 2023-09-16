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
for article in content["articles"]:
    print(article["title"])
    print(article["description"])