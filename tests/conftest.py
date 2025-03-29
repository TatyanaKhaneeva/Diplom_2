import pytest
import requests
from data.URLs import login, change_user_data, create_user, delete_user_url, ingredients_url
from helper.helper import Helper

@pytest.fixture
def generate_random_data():
    helper = Helper()
    email = helper.generate_random_email()
    password = helper.generate_random_string(10)
    name = helper.generate_random_string(10)
    user_data = {
        "email": email,
        "password": password,
        "name": name
    }
    return user_data



@pytest.fixture
def delete_user():
    def _delete_user(user_data, access_token):
        yield


        requests.delete(login, headers={"Authorization": f"Bearer {access_token}"})

    return _delete_user


@pytest.fixture
def create_and_login_user(generate_random_data):
    user_data = generate_random_data
    requests.post(create_user, json=user_data)
    response_login = requests.post(login, json=user_data)
    token = response_login.json().get("accessToken")
    yield {"user_data": user_data, "accessToken": token}

    requests.delete(delete_user_url, headers={"Authorization": f"Bearer {token}"})


@pytest.fixture(scope="session")
def ingredients():
    response = requests.get(ingredients_url)
    response.raise_for_status()
    return response.json()["data"]
