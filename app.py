# Import Dependancies
from flask import Flask

# Create a new instance
app = Flask(__name__)

# Create Flask Routes
@app.route('/')
def hello_world():
    print("Hello, World!")