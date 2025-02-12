"""
This module defines the backend API using Flask.
"""

from flask import Flask, request, jsonify
from database.data_manager import load_users, save_user
from services.match_service import find_matches
from services.message_service import send_message, get_messages

app = Flask(__name__)
@app.route("/login", methods=["POST"])
def login():
    """
    Authenticates a user using email and password.

    Returns:
        JSON response with success message and user ID.
    """
    data = request.json
    users = load_users()

    for user in users:
        if user["email"] == data["email"] and user["password"] == data["password"]:
            return jsonify({"success": True, "user_id": user["id"]}), 200

    return jsonify({"success": False, "message": "Invalid credentials"}), 401

@app.route("/register", methods=["POST"])
def register():
    """
    Registers a new user in the JSON database.
    
    Returns:
        JSON response with a success message.
    """
    data = request.json
    save_user(data)
    return jsonify({"message": "User registered successfully."}), 201

@app.route("/matches/<int:user_id>", methods=["GET"])
def get_matches(user_id):
    """
    Retrieves matching users based on language and interests.
    
    Args:
        user_id (int): The ID of the user.

    Returns:
        JSON response with a list of matches.
    """
    users = load_users()
    current_user = next((u for u in users if u["id"] == user_id), None)
    
    if current_user:
        matches = find_matches(current_user)
        return jsonify(matches), 200
    return jsonify({"error": "User not found"}), 404

@app.route("/messages/send", methods=["POST"])
def send_message_route():
    """
    Sends a message from one user to another.
    
    Returns:
        JSON response confirming the message was sent.
    """
    data = request.json
    if send_message(data["sender_id"], data["receiver_id"], data["message"]):
        return jsonify({"message": "Message sent successfully"}), 200
    return jsonify({"error": "Failed to send message"}), 400

@app.route("/messages/<int:user_id>", methods=["GET"])
def get_messages_route(user_id):
    """
    Retrieves messages for a specific user.
    
    Args:
        user_id (int): The ID of the user.

    Returns:
        JSON response with the list of messages.
    """
    messages = get_messages(user_id)
    return jsonify(messages), 200

if __name__ == "__main__":
    app.run(debug=True)
