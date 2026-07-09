# The first test suite.
# Adding and retrieving a Pet

# Fixtures are retrieved automatically from conftest.py

# Actual tests start here
def test_add_pet(fresh_pet_response, pet_id):
    # Pet should already be created via the fixture.
    creation_json = fresh_pet_response.json()
    
    assert fresh_pet_response.status_code == 200
    assert creation_json['id'] == pet_id
    assert creation_json['name'] == 'Gordon'
    assert creation_json['tags'][0]['name'] == 'friendly'
    assert creation_json['photoUrls'][0] == 'https://jonathanclede.com/img/gordon_puppy.png'

def test_retrieve_pet(pet_retrieval_response, pet_id):
    retrieval_json = pet_retrieval_response.json()
    assert pet_retrieval_response.status_code == 200
    assert retrieval_json['id'] == pet_id
    assert retrieval_json['name'] == 'Gordon'
    assert retrieval_json['tags'][0]['name'] == 'friendly'
    assert retrieval_json['photoUrls'][0] == 'https://jonathanclede.com/img/gordon_puppy.png'

def test_retrieve_nonexistent_pet(pet_exists, nonexistent_pet_retrieval_response):
    # Pet should not exist, since we cleared it via the fixture.
    assert pet_exists() == False
    assert nonexistent_pet_retrieval_response.status_code == 404