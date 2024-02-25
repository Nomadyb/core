import requests
from pprint import pprint

# {'key': '9e8b61fd6d5b5dbc81ecabc25f23fa0076605115'}
def client():
    credentials = {
        "username":"nomadaeyb",
        "password":"4a237237rock"
    }

    response = requests.post (
        url=  "http://127.0.0.1:8000/api/rest-auth/login/",
        data = credentials

    )

    print("Status Code:",response.status_code)
    response_data = response.json()
    pprint(response_data)


if __name__ == "__main__":
    client()