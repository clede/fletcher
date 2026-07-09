# Tests for updating an existing pet.

import pytest

# Fixtures will be retrieved automatically from conftest.py

# Actual tests start here

def test_update_pet(pet_update_response, pet_retrieval_response, pet_id):
	retrieval_json = pet_retrieval_response.json()
	assert pet_retrieval_response.status_code == 200
	assert retrieval_json['id'] == pet_id
	assert retrieval_json['tags'][0]['name'] == 'surly'
	assert retrieval_json['photoUrls'][0] == 'https://jonathanclede.com/img/bounder_cat.png'
	assert retrieval_json['name'] == 'Bounder'

@pytest.mark.xfail(reason="Known issue: Petstore sample server returns 200 instead of 404, contrary to spec.")
def test_update_nonexistent_pet(nonexistent_pet_update_response):
	# The API should return a 404 if the pet didn't exist before the update.
	assert nonexistent_pet_update_response.status_code == 404
