"""
This module manages user messaging.
"""

import json
import os

MESSAGE_DB = "database/messages.json"

def load_messages():
    """
    Loads messages from the JSON file.
    
    Returns:
        list: List of messages.
    """
    if not os.path.exists(MESSAGE_DB):
        return []
    
    with open(MESSAGE_DB, "r", encoding="utf-8") as f:
        return json.load(f)

def save_message(message):
    """
    Saves a message to the JSON database.
    
    Args:
        message (dict): Message data.
    """
    messages = load_messages()
    messages.append(message)

    with open(MESSAGE_DB, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=4)

def send_message(sender_id, receiver_id, message):
    """
    Sends a message from one user to another.
    
    Args:
        sender_id (int): Sender's ID.
        receiver_id (int): Receiver's ID.
        message (str): Message content.

    Returns:
        bool: True if the message was saved successfully.
    """
    msg = {
        "sender_id": sender_id,
        "receiver_id": receiver_id,
        "message": message
    }
    save_message(msg)
    return True

def get_messages(user_id):
    """
    Retrieves messages for a specific user.
    
    Args:
        user_id (int): The ID of the user.

    Returns:
        list: List of messages received by the user.
    """
    messages = load_messages()
    return [m for m in messages if m["receiver_id"] == user_id]
