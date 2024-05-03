import smtplib
import secrets
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, jsonify, request
from pymongo import MongoClient
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_cors import CORS
from bson import ObjectId
from bson.errors import InvalidId  
from datetime import datetime, timedelta
import threading 

# the threading libry is used to create a mutual exclusion lock


app = Flask(__name__)
app.secret_key = "jumpstart@dev"

CORS(app)
client = MongoClient("mongodb+srv://lonfonyuyromaric:sWIOt8pzIIRzWSoq@cluster0.0yayono.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.jumpstart

print("Connected to the database successfully!")

def send_email(email, token):
    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("lonfonyuyromeo@gmail.com", "b2qh2699,")

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = "lonfonyuyromeo@gmail.com"
    msg['To'] = email
    msg['Subject'] = "Your token. Note that this token will expire in 39 minutes"
    body = f"Your token is {token}"
    msg.attach(MIMEText(body, 'plain'))

    
    server.send_message(msg)
    server.quit()

@app.route("/")
def Home():
    return "Welcome to the marks corrections system"

@app.route('/register/<userId>', methods=['POST'])
def register_user(userId):
    data = request.json
    user = db.users.find_one({"email": data['email']})
    token = secrets.token_hex(16)
    if user:
        # send_email(data['email'], token)
        return jsonify({"error": "User already exists", "token": token}), 400
    else:
        user = {
            "  email": data['email'],
        }
        
        create_user = db.users.insert_one(user)
        # send_email(data['email'], token)
        return jsonify({"message": "User created successfully", "user_id": str(create_user.inserted_id), "token": token}), 201


@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    user = db.users.find_one({"email": data['email']})
    if user:
        return jsonify({"message": "User logged in successfully"}), 200
    else:
        
        user = {
            "email": data['email'],
        }
        
        create_user = db.users.insert_one(user)
        # send_email(data['email'], token)
        return jsonify({"message": "User created successfully", "user_id": str(create_user.inserted_id)}), 200


@app.route('/get_users', methods=['GET'])
def get_users():
    users = db.users.find()
    response = []
    for user in users:
        user['_id'] = str(user['_id'])
        response.append(user)
    return jsonify(response), 200

@app.route('/get_user/<email>', methods=['GET'])
def get_user(email):
    user = db.users.find_one({"email": email})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404



# @app.route('/create_request/<userId>', methods=['POST'])
# def create_request(userId):
    
#     try:
#         data = request.json
#         user_request = {
#             "userId": ObjectId(userId),
#             "name": data['name'],
#             "age": data['age'],
#             "level": data['level'],
#             "topic": data['topic'],
#             "message": data['message'],
#             "status": "Pending",
#             "created_at": datetime.now()
#         }
#         create_request = db.requests.insert_one(user_request)
#         return jsonify({"message": "Request created successfully", "request_id": str(create_request.inserted_id), "user_id": str(user_request["userId"])}), 201
#     except InvalidId:
#         return jsonify({"error": "Invalid user ID format"}), 400





# Mutex for mutual exclusion
mutex = threading.Lock()

@app.route('/create_request/<userId>', methods=['POST'])
def create_request(userId):
    try:
        # Acquire the lock, so that no any other user can enter this bloc
        # untill one user has successfully completed the request creation.
        mutex.acquire()
        
        data = request.json
        user_request = {
            "userId": ObjectId(userId),
            "name": data['name'],
            "age": data['age'],
            "level": data['level'],
            "topic": data['topic'],
            "message": data['message'],
            "status": "Pending",
            "created_at": datetime.now()
        }

        # Check the last request made by the user
        last_request = db.requests.find_one({"userId": ObjectId(userId)}, sort=[("created_at", -1)])

        # If the last request was made less than 3 days ago, return an error message
        if last_request and last_request["created_at"] > datetime.now() - timedelta(days=3):
            return jsonify({"error": "You can only create a new request if 3 days have passed since the last request"}), 400

        # If the last request was made 3 or more days ago, proceed to create the request
        create_request = db.requests.insert_one(user_request)
        
        # Release the lock, so that other users can enter this block and try to create a request
        mutex.release()

        return jsonify({"message": "Request created successfully", "request_id": str(create_request.inserted_id), "user_id": str(user_request["userId"])}), 201
    except InvalidId:
        # Release the lock in case of error
        mutex.release()
        return jsonify({"error": "Invalid user ID format"}), 400


@app.route('/get_requests/<userId>', methods=['GET'])
def get_requests(userId):
    try:
        user_id = ObjectId(userId)
    except InvalidId:
        return jsonify({"error": "Invalid user ID format"}), 400

    requests = db.requests.find({"userId": user_id})

    
    requests_list = []
    for request in requests:
        request['_id'] = str(request['_id'])  
        request['userId'] = str(request['userId'])  
        requests_list.append(request)

    return jsonify(requests_list), 200


if __name__ == "__main__":
    app.run(debug=True)