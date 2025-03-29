import requests
import pytest
import allure


class TestLogin:

    @allure.title('Логин под существующим пользователем')
    def test_login_existing_user(self):
        url = "https://stellarburgers.nomoreparties.site/api/auth/login"
        payload = {
            "email": "my_unique_user@yandex.ru",
            "password": "existingpassword"
        }
        with allure.step("Отправка запроса на логин"):
            response = requests.post(url, json=payload)
        with allure.step("Проверка статуса ответа и наличия токена"):
            assert response.status_code == 200
            assert "accessToken" in response.json()

    @allure.title('Логин с неверным логином и паролем')
    def test_login_with_incorrect_credentials(self):
        url = "https://stellarburgers.nomoreparties.site/api/auth/login"
        payload = {
            "email": "incorrect@example.com",
            "password": "incorrectpassword"
        }
        with allure.step("Отправка запроса с неверными данными"):
            response = requests.post(url, json=payload)
        with allure.step("Проверка статуса ответа и сообщения"):
            assert response.status_code == 401
            assert response.json()["message"] == "email or password are incorrect"