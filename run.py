from flaskblog import app

#Use this in order to run the app through python
#Using this avoids the hassle in creating and
#utilizing env. variables
if __name__ == '__main__':
    app.run(debug=True)