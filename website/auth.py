from flask import Blueprint, render_template # this file is a blueprint of our app that has all of the routes for our website

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/register')
def register():
    return render_template("register.html")