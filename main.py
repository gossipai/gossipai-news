import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import requests
import json

cred = credentials.Certificate("gossipai-server-firebase-adminsdk-rasja-b50b600f22.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def create_document():

    url = "https://newsapi.ai/api/v1/minuteStreamArticles?query=%7B%22%24query%22%3A%7B%22%24or%22%3A%5B%7B%22lang%22%3A%22eng%22%7D%2C%7B%22lang%22%3A%22tur%22%7D%2C%7B%22lang%22%3A%22deu%22%7D%5D%7D%2C%22%24filter%22%3A%7B%22isDuplicate%22%3A%22skipDuplicates%22%7D%7D&apiKey=15612acc-18f1-4014-83a2-db4d45297aa7&callback=JSON_CALLBACK"

    response = requests.get(url)
    response_text = response.text[14:-1]
    news = json.loads(response_text)

    # Save the news to Firestore
    for article in news["recentActivityArticles"]["activity"]:
        news_ref = db.collection('news').document()
        condensed_article = {
            "uri": article["uri"],
            "title": article["title"],
            "body": article["body"],
            "dateTime": article["dateTime"],
            "source": article["source"]["title"],
            "sourceUri": article["source"]["uri"],
            "url": article["url"],
            "image": article["image"],
            "language": article["lang"]
        }
        news_ref.set(condensed_article)

    print("Created a new document in 'news' collection.")

while True:
    create_document()
    time.sleep(7200)