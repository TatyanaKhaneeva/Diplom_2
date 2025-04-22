import pytest
import requests
from data.URLs import login, create_user, delete_user_url, ingredients_url
from helper.helper import Helper



@pytest.fixture
def delete_user():
    user_data = None
    access_token = None
    yield {"user_data": user_data, "access_token": access_token}
    if user_data and access_token:
        requests.delete(login, headers={"Authorization": f"Bearer {access_token}"})


@pytest.fixture
def create_and_login_user():
    helper = Helper()
    email = helper.generate_random_email()
    password = helper.generate_random_string(10)
    name = helper.generate_random_string(10)
    user_data = {
        "email": email,
        "password": password,
        "name": name
    }
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
