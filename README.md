# Purpose of this project

This project is a Web Application and its goal is to automate the making of web pages by using Flask, Jinja2, Html, Bootstrap  and to enable its users to possess their own web pages
after they create an account.

## About the main page
When a new user accesses this Web Appliaction, the user will be automatically redirected to the Main Page. Here a message will appear informing the user that an account
is required before the user can continue. On the same page, there is a navigation bar which the user can user to either create a new account or log in(provided that the
user has already an account)

## About the Sign-Up and Log In pages
On both of these pages, the user will need to fill a form in order to either create a new account or log in. If the user is on the Sign-Up Page and creates a new account,
the input from the form will be stored to a Sql Database in order to save the new account. Then the user will be redirected to the log in page where a new form will appear.

After a successfull log in, the user will be redirected to the Generate Server Page.

## About the Generate-Server Page
Here the user will need to create their own web page and manually input the following:  Server_Name, Server_Password, Server_Color and the Player_Limit. After saving these
settings, the user will finally be redirected to their own webpage.

## How the web page is generated
Whenever a new user creates a web page and inputs the settings through a form, the Account name and the Server Settings are all moved and stored inside a second Sql Database.
After that, they will be automatically redirected to their own webpage.

However it's worth mentioning that each new user has to manually log in again after they create a new webpage for the first time, otherwise the server settings won't be visible to the user
and the settings will not be printed to the screen! After they manually log in again by using the navigation bar, they will be rediected one last time to their own Web Page and now the server
settings that they used will finally appear on the screen.

## Final thoughts
By using two separate Sql Databases, the server is able to store both the new accounts of the user and the server settings. By doing this, whenever an old user appears, they
will be automatically recognized by the server and redirected to their web pages. Also, all the new users will be stored to the database so that they can successfully log in
later. 

All in all, this project was created for fun and its main goal was to dinamically and automatically generate Web Pages for each user and help them save a lot of time, instead of letting the
users  create their own web pages by using different technologies like Word Press or different Programing Languages, which would take some time.


