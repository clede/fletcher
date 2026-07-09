# Reusable constants (and variables that act like constants)

API_KEY = "special-key"
BASE_URL = "https://petstore.swagger.io/v2"
HEADERS = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "api_key": f"{API_KEY}",
        }

pet_id = 473089602