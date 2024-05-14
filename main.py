import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import os

cred = credentials.Certificate("gossipai-server-firebase-adminsdk-rasja-b50b600f22.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def create_document():
    news_ref = db.collection('news').document()
    news_ref.set({})
    print("Created a new document in 'news' collection.")

while True:
    create_document()
    time.sleep(60)