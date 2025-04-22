import requests
import random
import string
from data.URLs import create_user

def generation_new_data_user():
    letters = string.ascii_lowercase
    login_new = ''.join(random.choice(letters) for i in range(10))
    password_new = ''.join(random.choice(letters) for i in range(10))
    name_new = ''.join(random.choice(letters) for i in range(10))

    return {"login": login_new, "password": password_new, "firstName": name_new}


def register_new_user_and_return_login_password():

    login_pass = []

    data = generation_new_data_user()
    login = data["login"]
    password = data["password"]
    name = data["name"]

    payload = {
        "login": login,
        "password": password,
        "name": name
    }

    response = requests.post(f"{create_user}", data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(name)

    return login_pass