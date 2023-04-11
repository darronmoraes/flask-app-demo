from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_mysqldb import MySQL

# Initialize app
app = Flask(__name__)




# default route
@app.route('/', methods=['GET'])
def index():
    return jsonify("Hello World!")







# run server
if __name__ == '__main__':
    app.run(debug=True)