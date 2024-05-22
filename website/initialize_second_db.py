import mysql.connector
from datetime import datetime


#This function searches to see if the current account is stored inside the second database
def search_for_user(account_name, add_user, new_server_settings):
    #Connecting python to Sql
    try:
        db2 = mysql.connector.connect(
            host='localhost',
            user='root',
            password='bananaverde3',
            database='Database2'
        )
    except mysql.connector.Error as err:
        print('Error, could not connect to the second database, reason : {}', format(err))

    grabbed_settings = []

    #Searching for the account
    cursor = db2.cursor()
    cursor.execute('SELECT User FROM Servers_Settings_And_Users')
    rows = cursor.fetchall()

    for users in rows:
        stored_user = users[0]

        if account_name == stored_user and not add_user:
            # If the account exists, we will retrieve the server settings for that user
            cursor.execute("SELECT * FROM Servers_Settings_And_Users WHERE User='" + account_name + "'")
            server_settings = cursor.fetchall()

            # Storing the server settings to a list of strings and returning them
            for settings in server_settings:
                grabbed_settings.append(", ".join(map(str, settings)))
            return grabbed_settings, True

        if add_user:

            # If we have a new user we will add it to the table along with the server settings
            cursor.execute(
                'INSERT INTO Servers_Settings_And_Users (User,Server_Name,Server_Password,Color,Player_Limit) VALUES (%s,%s,%s,%s,%s)',
                (
                    new_server_settings[0], new_server_settings[1], new_server_settings[2], new_server_settings[3],
                    new_server_settings[4]
                ))
            db2.commit()
            return [], True


    #After the Get request, it the account was not found, we will return an empty list and False
    return [], False






























