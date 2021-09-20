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
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            flash("Username Already Registered!")
            return redirect(url_for("signup"))

        signup = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
            "birthday": request.form.get("birthday"),
            "username": request.form.get("username").lower()
        }
        mongo.db.users.insert_one(signup)

        session["user"] = request.form.get("username").lower()
        flash("You Are Now Registered With Us!")
        return redirect(url_for("buddies_area", username=session["user"]))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome Back {}".format(request.form.get("username")))
                    return redirect(url_for("buddies_area", username=session["user"]))
            else:
                flash("Oops! Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Oops! Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/buddies_area/<username>", methods=["GET", "POST"])
def buddies_area(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session["user"]:
        return render_template("buddies_area.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("Hope to see you back soon!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_your_event", methods=["GET", "POST"])
def add_your_event():
    if request.method == "POST":
        event = {
            "type_of_event": request.form.get("type_of_event"),
            "event_name": request.form.get("event_name"),
            "type_of_music": request.form.get("type_of_music"),
            "event_date": request.form.get("event_date"),
            "event_location": request.form.get("event_location"),
            "created_by": session["user"]
        }
        mongo.db.yourEvents.insert_one(event)
        flash("Your Event Has Been Added :)")
        return redirect(url_for("buddies_area", username=session["user"]))

    music = mongo.db.music.find().sort("type_of_music", 1)
    events = mongo.db.events.find().sort("type_of_event", 1)
    return render_template("add_your_event.html", music=music, events=events)


@app.route("/edit_your_event/<yourEvent_id>", methods=["GET", "POST"])
def edit_event(yourEvent_id):
    if request.method == "POST":
        edit = {
            "type_of_event": request.form.get("type_of_event"),
            "event_name": request.form.get("event_name"),
            "type_of_music": request.form.get("type_of_music"),
            "event_date": request.form.get("event_date"),
            "event_location": request.form.get("event_location"),
            "created_by": session["user"]
        }
        mongo.db.yourEvents.update({"_id": ObjectId(yourEvent_id)}, edit)
        flash("Your Event Has Been Updated :)")
    
    yourEvent = mongo.db.yourEvents.find_one({"_id": ObjectId(yourEvent_id)})

    music = mongo.db.music.find().sort("type_of_music", 1)
    events = mongo.db.events.find().sort("type_of_event", 1)
    return render_template(
        "edit_your_event.html", yourEvent=yourEvent, music=music, events=events)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)