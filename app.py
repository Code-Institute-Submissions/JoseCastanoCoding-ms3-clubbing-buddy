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


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    return redirect(url_for("buddies_area", username=session["user"]))
            else:
                return redirect(url_for("/login"))
        
        else:
            return redirect(url_for("login"))
    
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)