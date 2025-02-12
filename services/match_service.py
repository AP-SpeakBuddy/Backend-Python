"""
This module handles user matching logic.
"""

from database.data_manager import load_users

def find_matches(current_user):
    """
    Finds matching users based on language preferences.
    
    Args:
        current_user (dict): The user's data.

    Returns:
        list: List of matching users.
    """
    users = load_users()
    matches = []

    for user in users:
        if user["id"] != current_user["id"]:
            if user["speaks"] == current_user["learning"] and \
               user["learning"] == current_user["speaks"]:
                matches.append(user)

    return matches
