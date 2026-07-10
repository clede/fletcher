# Reusable client wrapper functions

import sys
import os
import requests
import json
from pathlib import Path
from constants import BASE_URL, HEADERS

sys.path.insert(0, os.path.join(os.path.dirname(__file__), """..""", 'data'))
from pet_ids import pet_id

payloads_path = Path(__file__).parent / """..""" / 'data' / 'pet_payloads.json'

# Set up pet data to be used throughout the tests.
with open(payloads_path, 'r') as payloads:
    pets = json.load(payloads)
for pet in pets:
    pet['id'] = pet_id
new_pet = pets[0]
updated_pet = pets[1]

# Functions start here.
def get_pet(id=pet_id):
    """Gets an existing pet."""
    resp = requests.get(
        f'{BASE_URL}/pet/{id}',
        headers = HEADERS,
        timeout = 30
    )
    return resp

def pet_exists(id=pet_id):
    """Checks if a pet exists already or not."""
    return get_pet(id).status_code == 200

def delete_pet(id=pet_id):
    """Deletes a pet."""
    resp = requests.delete(
        f'{BASE_URL}/pet/{id}',
        headers = HEADERS,
        timeout = 30
    )
    return resp
    
def create_pet():
    """Add a new pet. Currently only uses the predefined pet_id. 
    Return the response object."""
    resp = requests.post(
        f'{BASE_URL}/pet',
        headers = HEADERS,
        json = new_pet,
        timeout = 30
    )
    return resp
    
def update_pet():
    """Updates an existing pet. Returns the API's response even if the original 
    pet didn't exist"""
    
    resp = requests.put(
        f'{BASE_URL}/pet',
        headers = HEADERS,
        json = updated_pet,
        timeout = 30
    )
        
    return resp