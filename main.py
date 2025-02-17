import requests

api_key = ""
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])