import mysql.connector
from flask import request

def store_data(cursor, account_data, db):
    found_username = False

    #Get all the names from the database table
    cursor.execute('SELECT Name FROM Users')
    for names in cursor:
        stored_name = names[0]
        #If the username already exists inside the database, return True
        if account_data[0] == stored_name:
            found_username = True

    #If the username already exists, return true
    if found_username:
        return True
    else:
        # Storing all the new accounts to database if the request is POST
        cursor.execute('INSERT INTO Users (Name,Password,Email) VALUES (%s,%s,%s)', (account_data[0], account_data[1], account_data[2]))
        db.commit()
        return False


#This function checks if the accounts exists and if the current accounts has the right credentials
def check_account(current_account, cursor):
    current_username = current_account[0]
    current_password = current_account[1]

    #Searching for an account inside database that corresponds to the username entered via form
    cursor.execute("SELECT * FROM Users WHERE Name='" + current_username + "'")
    #Storing the row found to the variable 'table_row'
    table_row = cursor.fetchone()

    #If the username and password correspond to the table row, return True
    if table_row and table_row[2] == current_password:
        return True
    return False


def create_connector(account_data, current_route):
    username_already_in_use = False
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
                username_already_in_use = store_data(cursor, account_data, db)
            except mysql.connector.Error as err:
                # If data could not be stored inside the database, print the error
                print("Error storing data to database {}", format(err))
            finally:
                # Regardless of whether an exception was raised or not, close the database connection if it exists
                if 'db' in locals() or 'db' in globals():
                    db.close()

            return True if username_already_in_use else False

        #If the user wants to log in, call check_account function
        if request.method == 'POST' and current_route == 'log_in':
            account_found = check_account(account_data, cursor)
            return account_found
