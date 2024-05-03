from flask import Flask, jsonify, request
from pymongo import MongoClient
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_cors import CORS
from bson import ObjectId

app = Flask(__name__)
app.secret_key = "jumpstart@dev"

CORS(app)
# Replace <connection_string> and <database_name> with your actual values
# client = MongoClient("mongodb+srv://lonfonyuyromaric:Kb1gPE7WgtqIeLSc@deplan.y85aa1q.mongodb.net/?retryWrites=true&w=majority")
client = MongoClient("mongodb+srv://lonfonyuyromaric:sWIOt8pzIIRzWSoq@cluster0.0yayono.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.jumpstart


print("Connected to the database successfully!")


@app.route("/")
def Home():
    return "Welcome to the marks corrections system"




    