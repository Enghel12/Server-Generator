import mysql.connector
from flask import request
from datetime import datetime


def store_data(cursor, account_data, db):

    #Getting all the usernames stored inside the database
    cursor.execute('SELECT Username FROM Users')
    for names in cursor:
        stored_name = names[0]
        # If the username already exists inside the database, raise an exception
        if account_data[0] == stored_name:
            raise ValueError("Username already in use, please use a different one")


    #Getting all the emails stored inside the database
    cursor.execute('SELECT Email FROM Users')
    for emails in cursor:
        stored_email = emails[0]
        # If the email is already in use raise an exception
        if account_data[2] == stored_email:
            raise ValueError("Email already in use, please use a different one")


    # Storing all the new accounts to database if the request is POST
    cursor.execute('INSERT INTO Users (Username,Password,Email) VALUES (%s,%s,%s)', (account_data[0], account_data[1], account_data[2]))
    db.commit()



#This function checks if the accounts exists and if the current accounts has the right credentials
def check_account(current_account, cursor):
    cursor.execute('SELECT * FROM Users')
    table_rows = cursor.fetchall()

    current_username = current_account[0]
    current_password = current_account[1]

    #Searching for an account inside database that corresponds to the username entered via form
    cursor.execute("SELECT * FROM Users WHERE Username='" + current_username + "'")
    #Storing the row found to the variable 'table_row'
    table_row = cursor.fetchone()

    #If the username and password correspond to the table row, return True
    if table_row and table_row[1] == current_password:
        #Getting the id of the user after logging in to search for it in the second database
        return True
    return False


def create_connector(account_data, current_route):

    try:
        #Creating a connection between the database called Accounts and Python by using a Mysql connector
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='bananaverde3',
            database='Accounts'
        )
    except mysql.connector.Error as err:
        #If the server could not connect to the database, print the error
        print("Error connecting to database {}", format(err))
        return
    else:
        cursor = db.cursor()

        #If the user wants to sign_up, call the function store_data
        if request.method == 'POST' and current_route == 'sign_up':
            try:
                store_data(cursor, account_data, db)
            except mysql.connector.Error as err:
                # If data could not be stored inside the database, print the error
                print("Error storing data to database {}", format(err))

            # Regardless of whether an exception was raised or not, close the database connection if it exists
            db.close()


        #If the user wants to log in, call check_account function
        if request.method == 'POST' and current_route == 'log_in':
            account_found = check_account(account_data, cursor)
            return account_found
