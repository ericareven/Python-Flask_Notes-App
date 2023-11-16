from flask import Blueprint # this file is a blueprint of our app that has all of the routes for our website

views = Blueprint('views', __name__)

@views.route('/') # homepage url
def home():
    return '<h1>Test</>'
