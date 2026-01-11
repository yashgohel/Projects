import requests
query = input("What type of news are you interested today? ")
api = "99dcbd81fa6f476598f8fc67471910c3"

url = f"https://newsapi.org/v2/everything?q=apple&from=2025-12-20&to=2025-12-20&sortBy=popularity&apiKey={api}"

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n------------------------------------\n")