# Project Purpose
This project is a web application designed to automate web page creation using Flask, Jinja2, HTML, and Bootstrap. It allows users to have their own web pages after creating an account.

## Main Page
When accessing the application, new users are redirected to the Main Page. A message informs them that an account is required to continue. The navigation bar on this page allows users to either create a new account or log in if they already have one.

## Sign-Up and Log In Pages
Users fill out a form on these pages to create an account or log in. When creating a new account on the Sign-Up Page, the form data is stored in a SQL database, and users are redirected to the Log In Page to log in. After a successful log in, users are redirected to the Generate Server Page.

## Generate Server Page
On this page, users create their web page by inputting details like Server Name, Server Password, Server Color, and Player Limit. After saving these settings, users are redirected to their own web page.

## Generating User Web Pages
When a web page is created, the account name and server settings are stored in a second SQL database. Users are redirected to their web page, but they must log in again to see the server settings. Once logged in, the settings will appear on the screen.

## Final Thoughts
Using two SQL databases, the server stores both user accounts and server settings. This allows returning users to be recognized and redirected to their web pages. The project aims to save time by automating web page creation, avoiding the need for users to manually create pages with other technologies like WordPress or different programming languages.







