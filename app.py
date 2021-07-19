# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getImageUrlFrom
import os

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

# add route for your gif results
@app.route('/yourgif', methods = ["GET", "POST"])
def yourgif():
    user_response = "dog"
    gifLink = getImageUrlFrom(user_response)
    print(gifLink)
    
    #pass URL to render template and have that URL appear as an image in yourgif.html

    # get the gif for giphy and puts the link on the webpage
    return render_template("yourgif.html", time = datetime.now(), gifLink = gifLink)
    # add datetime.now() to trick our browser into updating the css if we make any changes

    