from flask import Blueprint, redirect, url_for, render_template

#Creating a blueprint called views
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('Home.html')

@views.route('/admin')
def admin():
    #Redirect the user if he/she tries to access admin route without being the admin
    return redirect(url_for('views.home'))

#Creating an Easter egg view that will execute when the user accesses a secret route
@views.route('/admin/ID')
def hidden_page():
    #Printing the secret text to the user
    return "<h1>You shouldn't be here!</h1>"








