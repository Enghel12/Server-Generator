from flask import Blueprint, redirect, url_for, render_template, request, flash, session
from website import initialize_second_db



#Creating a blueprint called views
views = Blueprint('views', __name__)

@views.route('myServer.html/<current_user>', methods=['POST', 'GET'])
def user_server(current_user):

    # Getting the server settings from the session and storing them to a string
    server_settings = session.get('server_settings', None)

    current_settings = server_settings[0].split()

    # Passing the server settings to the user's web page
    return render_template('User_Server.html', settings = current_settings)


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

@views.route('/Generate-Server/<account_name>', methods=['POST', 'GET'])
def generate_server(account_name):
    if request.method == 'GET':
        #Checking to see if the current user is stored in the second database
        response = initialize_second_db.search_for_user(account_name, False, [])

        #If we found the user and grabbed the server settings we will redirect the user to the new page
        if response[1]:
            #Storing the server settings to session
            session['server_settings'] = response[0]
            return redirect(url_for('views.user_server', current_user=account_name))
        else:
            return render_template('Generate-Server.html')

    else:
        #Getting the user input from the form
        server_name = request.form['server_name']
        server_password = request.form['server_password']
        color = request.form['color']
        player_limit = request.form['player_limit']


        #Checking to see if all the form was filled up
        if len(server_name) == 0 or len(server_password) == 0 or len(color) == 0 or len(player_limit) == 0:
            # If the user did not fill up a section of the form, redirect the user to the same page to try again
            flash('You must fill each section of the form! Try again', category='error')
            return render_template('Generate-Server.html')

        elif not player_limit.isdigit():
            # If the user did not use a valid number for the player limit, prompt the user to try again
            flash('Error, you did not use a valid number for the player limit, try again!', category='error')
            return render_template('Generate-Server.html')

        elif int(player_limit) > 20:
            # If the user tried to set the player limit above 20, redirect the user to the same page
            flash('Error, the player limit is a maximum of 20, please try again!', category='error')
            return render_template('Generate-Server.html')
        else:
            #If there is no problem with the form input we will store the server settings and the user to the database
            server_settings = [account_name,server_name,server_password,color,player_limit]
            # Storing the new user and the server settings from the form to the table
            initialize_second_db.search_for_user(account_name, True, server_settings)

            #Storing the new server settings to session
            session['server_settings'] = server_settings


            # Redirect the user to his server and print a new webpage to the screen
            return redirect(url_for('views.user_server', current_user=account_name))

        #If the request is post but the user did not fill correctly the form, redirect the user to the same page
        return render_template('Generate-Server.html')

