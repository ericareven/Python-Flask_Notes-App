from flask import Blueprint, render_template # this file is a blueprint of our app that has all of the routes for our website
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/') # homepage url
@login_required
def home():
    return render_template("home.html")

