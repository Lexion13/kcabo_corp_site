from flask import Flask, render_template,request,redirect,url_for # For flask implementation
from flask_sendgrid import SendGrid
import os

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

app.config['SENDGRID_API_KEY'] = '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'
app.config['SENDGRID_DEFAULT_FROM'] = 'info@kcabo.co.jp'
mail = SendGrid(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action/contact', methods=['POST'])
def contact():
    email = request.values.get('email')
    content = request.values.get('content')
    mail.send_email(
        from_email = 'info@@kcabo.co.jp',
        to_email = 'info@kcab.co.jp',
        subject = 'Subject',
        text = email+content
    )

    return redirect('/')

if __name__ == "__main__":
#    app.run(debug=True, host="localhost", port=8080)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, use_reloader=True, port=port)
