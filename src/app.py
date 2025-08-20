from flask import Flask, request, jsonify  # Importing Flask to create a web application\
from datetime import datetime  # Importing datetime to get the current time
import socket  # Importing socket to get the hostname of the machine
 # Importing request to handle incoming requests
 # Importing jsonify to return JSON responses
#from flask import Flask, jsonify


# Importing Flask to create a web application
app = Flask(__name__) # Creating an instance of the Flask class
# The Flask application is initialized here, and routes can be defined below
# This is the main application file for a Flask web application

@app.route('/api/v1/details') # Defining a route for the root URL
def details():
    return jsonify ({
        "message": "Hello, World!",
        "hostname": socket.gethostname(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
# This function returns a simple "Hello, World!" message when the root URL is accessed
@app.route('/api/v1/health')
def health():
    return jsonify({
        "status": "up",
        "code": 200 
    })
@app.route('/api/v1')
def index():
    return "<h1>Welcome to the Flask App!</h1>" 
 # This function returns a welcome message when the root URL is accessed

if __name__ == '__main__':
    app.run(debug=True) # Running the Flask application in debug mode


# Defining a simple route for the root URL
# @app.route('/')
# def index():
#     return "Welcome to the Flask App!" # This function returns a welcome message when the root URL is accessed  
# # Defining a route to handle GET requests at the '/api' endpoint
# @app.route('/api', methods=['GET'])
# def api():
#     # Extracting the 'name' parameter from the query string
#     name = request.args.get('name', 'World')
#     # Returning a JSON response with a greeting message
#     return jsonify({'message': f'Hello, {name}!'})
# Uncomment the following lines to add more routes
# '/apu/v1/health',
# '/apu/v1/healthz',
# '/apu/v1/metrics',
# '/apu/v1/status',
# '/apu/v1/ready',
# '/apu/v1/live',
# '/apu/v1/info',
# '/apu/v1/healthcheck',
# '/apu/v1/ping',
# '/apu/v1/status',








#'/apu/v1/details',
# '/apu/v1/health',
