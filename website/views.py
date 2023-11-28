from flask import Blueprint, render_template # this file is a blueprint of our app that has all of the routes for our website

views = Blueprint('views', __name__)

@views.route('/') # homepage url
def home():
    return render_template("home.html")

