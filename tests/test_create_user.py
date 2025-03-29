import requests
import allure

from data.URLs import create_user


class TestCreateUser:

    @allure.title('Создание уникального пользователя')
    def test_create_unique_user(self, generate_random_data, delete_user):
        payload = generate_random_data
        response = requests.post(create_user, json=payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

        user_data = response.json()["user"]
        access_token = response.json()["accessToken"]

        delete_user(user_data, access_token)


    @allure.title('Создание уже зарегистрированного пользователя')
    def test_create_existing_user(self):
        url = "https://stellarburgers.nomoreparties.site/api/auth/register"
        payload = {
            "email": "existinguser@example.com",
            "password": "existingpassword",
            "name": "Existing User"
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