from flask import Flask


app = Flask(__name__)

@app.route('/api/v1/mything')
def mything():
    return "Hello, World! This is mything endpoint."


if __name__ == "__main__":
    app.run(debug=True)
