from flask import Flask, render_template,request,redirect,url_for # For flask implementation
from pymongo import MongoClient # Database connector
from bson.objectid import ObjectId # For ObjectId to work
import feedparser
import os

app = Flask(__name__)

'''
client = MongoClient('localhost', 27017)    #Configure the connection to the database
db = client.kcabo    #Select the database
coll = db.coll #Select the collection
'''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action/contact', methods=['POST'])
def contact():
    email = request.values.get('email')
    content = request.values.get('content')
    return redirect('/')

if __name__ == "__main__":
#    app.run(debug=True, host="localhost", port=8080)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, use_reloader=True, port=port)
