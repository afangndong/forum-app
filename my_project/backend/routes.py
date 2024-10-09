from flask import Blueprint, request, jsonify
from models import db, User, Message

api = Blueprint('api', __name__)

@api.route('/signup', methods=['POST'])
def signup():
    data = request.json
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

@api.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@api.route('/post_message', methods=['POST'])
def post_message():
    data = request.json
    new_message = Message(user_id=data['user_id'], content=data['content'])
    db.session.add(new_message)
    db.session.commit()
    return jsonify({"message": "Message posted"}), 201

@api.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([{"user_id": msg.user_id, "username": msg.user.username,"content": msg.content} for msg in messages]), 200
