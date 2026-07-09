# Example of conftest.py file, containing all my reusable fixtures

import pytest
import sys
import os

# Allow us to import from files in the clients directory.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), """..""", 'clients'))

from pet_client import get_pet, pet_exists as _pet_exists, delete_pet, create_pet, pet_id as _pet_id, update_pet

# Basic pet setup fixtures.

@pytest.fixture
def clear_pet():
    """ Ensure we start with a clean slate: no pet. """
    if _pet_exists():
        delete_pet()

@pytest.fixture
def fresh_pet_response(clear_pet):
    """ Start with a newly created pet according to our standard setup. """
    # pet should automatically be cleared here.
    # and replaced by a new fresh pet.
    return create_pet()    

@pytest.fixture
def pet_id():
    return _pet_id

@pytest.fixture
def pet_retrieval_response(fresh_pet_response):
    """ Returns the response object for retrieving a newly-created pet. """
    return get_pet()

@pytest.fixture
def nonexistent_pet_retrieval_response(clear_pet):
    """ Returns the response object for retrieving a pet that doesn't exist. """
    return get_pet()

@pytest.fixture
def pet_exists():
    """ Returns the function to check if a pet exists or not. """
    return _pet_exists

@pytest.fixture
def delete_pet_fn():
    """ Returns the function to delete a pet. """
    return delete_pet

@pytest.fixture
def pet_update_response(fresh_pet_response):
    """ Returns the response object for updating a newly-created pet."""
    return update_pet()

@pytest.fixture
def nonexistent_pet_update_response(clear_pet):
    """ Returns the response object for updating a pet that doesn't exist."""
    return update_pet()