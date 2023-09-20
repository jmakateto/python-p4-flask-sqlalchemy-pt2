from flask import Flask, make_response
from models import db, Owner, Pet  # We'll come back to this in the next step

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1>Welcome to the pet/owner directory!</h1>', 200)
    return response

if __name__ == '__main__':
    app.run(port=5555)
