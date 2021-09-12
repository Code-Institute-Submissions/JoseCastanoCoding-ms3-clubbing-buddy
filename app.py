import os

import cloudinary
import cloudinary.uploader
import cloudinary.api

from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


cloudinary.config( 
  cloud_name = "jose-cloudinary", 
  api_key = "494171894259977", 
  api_secret = "Vn3TYGyC-vR_ULtIQCCxzWbSy7M" 
)


@app.route("/")
@app.route("/homepage.html")
def homepage():
    return render_template("homepage.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)