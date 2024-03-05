from website import create_app


app = create_app()

if __name__ == '__main__': 
    app.run(debug=True) # only if we run this file (not import it) will we execute this line

