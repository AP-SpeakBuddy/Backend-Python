"""
This module handles JSON database operations for users.
"""

import json
import os

USER_DB = "database/users.json"

def load_users():
    """
    Loads users from the JSON file.
    
    Returns:
        list: List of registered users.
    """
    if not os.path.exists(USER_DB):
        return []

    with open(USER_DB, "r", encoding="utf-8") as f:
        return json.load(f)

def save_user(user):
    """
    Saves a new user to the JSON database.
    
    Args:
        user (dict): User data.
    """
    users = load_users()
    user["id"] = len(users) + 1  # Generate unique ID
    users.append(user)

    with open(USER_DB, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)
