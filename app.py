"""
This file defines a FastAPI application that serves user data.
It loads data from `usuarios.json` and provides API endpoints.
 
Author: Mariam Betin <mbetine@udistrital.edu.co>
"""
import json
from fastapi import FastAPI, HTTPException

app = FastAPI()
USER_DATA_FILE = "data/usuarios.json"

def load_users():
    """ Loads users from the JSON file without modifications. """
    try:
        with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

@app.get("/users")
def get_users():
    """ Retrieves all users exactly as they are in `usuarios.json`. """
    users = load_users()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    
    return users

@app.get("/match/{user_id}")
def get_matches(user_id: int):
    """ Returns compatible users based on language preferences. """
    users = load_users()
    user = next((u for u in users if u["id"] == user_id), None)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    matches = [
        {
            "id": u["id"],
            "nombre": u["nombre"],
            "correo": u["correo"],
            "birthday": u["birthday"],
            "idioma_habla": u["idioma_habla"],
            "idioma_aprender": u["idioma_aprender"],
            "nivel_escritura": u["nivel_escritura"],
            "nivel_lectura": u["nivel_lectura"],
            "nivel_habla": u["nivel_habla"],
            "nivel_comprension": u["nivel_comprension"],
            "intereses": u["intereses"]
        }
        for u in users if u["idioma_aprender"] == user["idioma_habla"] and u["idioma_habla"] == user["idioma_aprender"]
    ]
    
    return matches
