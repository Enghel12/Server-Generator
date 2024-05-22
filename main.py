from website import create_app, auth, initialize_second_db

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)




