import requests
import allure
from helper.helper import Helper
from data.URLs import create_user


class TestCreateUser:

    @allure.title('Создание уникального пользователя')
    def test_create_unique_user(self, delete_user):
        helper = Helper()
        email = helper.generate_random_email()
        password = helper.generate_random_string(10)
        name = helper.generate_random_string(10)
        user_data = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(create_user, json=user_data)
        assert response.status_code == 200
        assert response.json()["success"] is True
        delete_user["user_data"] = response.json()["user"]
        delete_user["access_token"] = response.json()["accessToken"]


    @allure.title('Создание уже зарегистрированного пользователя')
    def test_create_existing_user(self, create_and_login_user):
        existing_user_data = create_and_login_user["user_data"]
        url = "https://stellarburgers.nomoreparties.site/api/auth/register"
        payload = {
            "email": existing_user_data["email"],
            "password": existing_user_data["password"],
            "name": existing_user_data["name"]
        }
        with allure.step("Отправка запроса на создание уже зарегистрированного пользователя"):
            response = requests.post(url, json=payload)
        with allure.step("Проверка статуса ответа и сообщения об ошибке"):
            assert response.status_code == 403
            assert response.json()["message"] == "User already exists"

    @allure.title('Создание пользователя с незаполненным обязательным полем')
    def test_create_user_with_missing_field(self):
        url = "https://stellarburgers.nomoreparties.site/api/auth/register"
        payload = {
            "password": "password",
            "name": "Missing Email"
        }
        with allure.step("Отправка запроса на создание пользователя с незаполненным полем"):
            response = requests.post(url, json=payload)
        with allure.step("Проверка статуса ответа и сообщения об ошибке"):
            assert response.status_code == 403
            assert response.json()["message"] == "Email, password and name are required fields"