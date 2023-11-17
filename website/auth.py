from flask import Blueprint # this file is a blueprint of our app that has all of the routes for our website

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/register')
def register():
    return "<p>Register</p>"