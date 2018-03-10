# Initial setup
from flask import Flask
import json

app = Flask(__name__)

# Index page 
@app.route("/")
def index():
	return_value = {"message":"Welcome to the Edu-Buddy API!"}
	json_string = json.dumps(return_value)
	return json_string

# Help page
@app.route("/help")
def help():
	return_value = {"message":"The available commands for this API will be visible here :)"}
	json_string = json.dumps(return_value)
	return json_string

# Error page
@app.errorhandler(404)
def page_not_found(e):
    return "No such avaiable command. Refer to the /help for more information.", 404

if __name__ == "__main__":
	app.debug = True
	app.run()
