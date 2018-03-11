# Initial setup

from flask import Flask, request, redirect, url_for



import json

import pyrebase



# Flask object creation

app = Flask(__name__)



# Firebase configuration

config = {

    "apiKey": "AIzaSyDNio_QK2oYeytYQ_6H1I4yQYzgFEuSWPg",

    "authDomain": "edubuddy-b7f29.firebaseapp.com",

    "databaseURL": "https://edubuddy-b7f29.firebaseio.com",

    "storageBucket": "edubuddy-b7f29.appspot.com",

}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
db = firebase.database()



# Index page

@app.route("/")

def index():

	return_value = {"message":"Welcome to the Edu-Buddy API!"}

	json_string = json.dumps(return_value)

	return json_string



# API page

@app.route("/api",methods = ['POST', 'GET'])

def api():

    json_string = "Anshul is great"+request.args.get('q')

    return json_string

    #return HttpResponse('<pre>' + r.text + 'Anshul is great </pre>'+full_url+" get try "+request.GET['q'])


# Database page

@app.route("/data",methods = ['POST', 'GET'])

def data():
        
        user_token = request.args.get('user_token')
        users = db.child("users").get(user_token)
        values  = users.val()
        json_string = json.dumps(values)
        
        return json_string


# Help page

@app.route("/help")

def help():

	return_value = {"message":"The available commands for this API will be visible here :)"}

	json_string = json.dumps(return_value)

	return json_string



# Authenticate user page

@app.route("/authenticate/", methods = ["GET"])

def authenticate_user():

	try:

		email = request.args.get('email')

		password = request.args.get('password')

		

		user = auth.sign_in_with_email_and_password(email, password)

		return_value = {"data":user['idToken']}

		json_string = json.dumps(return_value)

		return json_string

		

	except:

		return_value = {"message":"The user could not be succesfully authenticated."}

		json_string = json.dumps(return_value)

		return json_string



# User details page

@app.route("/user_details/", methods = ["GET"])

def user_details():

	try:

		user_token = request.args.get('user_token')

		account_information = auth.get_account_info(user_token)

		json_string = json.dumps(account_information)

			

		return json_string

	

	except:

		return_value = {"message":"The user details could not be retrieved."}

		json_string = json.dumps(return_value)

		return json_string

		

# Error page

@app.errorhandler(404)

def page_not_found(e):

	return_value = {"message":"No such avaiable command. Refer to the /help for more information."}

	json_string = json.dumps(return_value)

	return json_string, 404

    

if __name__ == "__main__":

	app.debug = True

	app.run()
