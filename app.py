from flask import Flask, render_template,request,redirect,url_for # For flask implementation
import os
import sendgrid

'''
from pymongo import MongoClient # Database connector
from bson.objectid import ObjectId # For ObjectId to work
import feedparser
'''

app = Flask(__name__)

'''
client = MongoClient('localhost', 27017)    #Configure the connection to the database
db = client.kcabo    #Select the database
coll = db.coll #Select the collection
'''
sendgrid_username = "app84049026@heroku.com"
sendgrid_password = "1211333s"



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action/contact', methods=['POST'])
def contact():
    email = request.values.get('email')
    content = request.values.get('content')
    sg = sendgrid.SendGridClient(sendgrid_username, sendgrid_password)
    message = sendgrid.Mail()
    message.add_to(email)
    message.set_subject("sendgrid_title")
    message.set_text(content)
    message.set_from('Kcabo inc.<info@kcabo.co.jp>')
    status,msg = sg.send(message)




    return redirect('/')

if __name__ == "__main__":
#    app.run(debug=True, host="localhost", port=8080)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, use_reloader=True, port=port)
