import os

import cloudinary
import cloudinary.uploader
import cloudinary.api

from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

cloudinary.config( 
  cloud_name = "jose-cloudinary", 
  api_key = "494171894259977", 
  api_secret = "Vn3TYGyC-vR_ULtIQCCxzWbSy7M" 
)

mongo = PyMongo(app)


@app.route("/")
@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)