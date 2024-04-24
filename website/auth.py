from flask import Blueprint, render_template, request, flash
from website import initialize_database
import re

#Creating a blueprint called auth
auth = Blueprint('auth', __name__)


#Creating new routes for the blueprint 'auth'
@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']

        #Calling this function to see if the current account exists
        account_data = [user, password]
        current_route = 'log_in'
        logged_in = initialize_database.create_connector(account_data, current_route)

        if logged_in:
            flash('You have successfully logged in', category='success')
            return render_template('login.html')
        else:
            flash('Failed to log in', category='error')
            return render_template('login.html')
    else:
        return render_template('login.html')


#The purpose of this function is to check the user input when creating an account
def validate_input(user, password, email):
    invalid_input = True

    #If any error occurs, the list will contain the error message
    if len(user) < 4:
        flash('Error, your username must be at least 4 characters long', category='error')
    elif len(password) < 8:
        flash('Error, your password must be at least 8 characters long', category='error')
    elif re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        flash('Error, your password must contain at least one special character like these: @, #, !, ..', category='error')
    elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        flash('Error, please enter a valid email address', category='error')
    elif len(email) < 4:
        flash('Error the email is too short', category='error')
    else:
        flash('Account created successfully!', category='success')
        invalid_input = False

    return invalid_input

@auth.route('/sign-up', methods=["POST", "GET"])
def sign_up():
    #If the request is post, we will retrieve the data from the form(the user input)
    if request.method == "POST":
        user = request.form['user']
        password = request.form['password']
        email = request.form['email']

        #Calling this function to validate user input
        invalid_input = validate_input(user, password, email)

        if invalid_input:
            #If input is invalid, redirect the user to the same page and ask for input again
            return render_template("/sign-up.html")
        else:
            #Storing the data to a python list
            account_data = [user, password, email]
            # Sending the form input to database to store the new account
            username_already_in_use = initialize_database.create_connector(account_data, 'sign_up')

            #If username already exists flash a message to the user
            if username_already_in_use:
                flash('Error, username is already in use,try a different one', category='error')

            return render_template('/sign-up.html')
    else:
        # If the request is get, we will just render the html web page to the user
        return render_template("/sign-up.html")
