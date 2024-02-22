from flask import Blueprint, render_template, request, flash # this file is a blueprint of our app that has all of the routes for our website

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greater than 3 characters,', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 characters,', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 6 characters,', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        else:
             # add user to datatbase
            flash('Account created!', category='success')
    return render_template("register.html")