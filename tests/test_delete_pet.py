# Placeholder for the second test suite.
# Deleting a pet

# Fixtures are retrieved automatically from conftest.py

# Actual tests start here
def test_delete_pet(fresh_pet_response, pet_exists, delete_pet_fn):
	# Make sure the pet exists before we go any further.
	assert pet_exists()
	
	assert delete_pet_fn().status_code == 200
	assert pet_exists() == False
	