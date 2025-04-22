import requests
import pytest
import allure
from helper.helper import Helper

class TestChangeData:

    helper = Helper()
    @pytest.mark.parametrize(
        "field, value", [("email", helper.generate_random_email()),
                         ("name", helper.generate_random_string(7))]
    )
    @allure.title('Изменение данных пользователя с авторизацией')

    def test_update_user_data_with_authorization(self, create_and_login_user, field, value):
        token = create_and_login_user['accessToken']
        url = "https://stellarburgers.nomoreparties.site/api/auth/user"

        payload = {
            field: value
        }
        with allure.step("Отправка запроса на обновление данных с токеном"):
            response = requests.patch(url, json=payload, headers={"Authorization": token})
        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 200
            assert response.json()["success"] == True
            assert response.json()["user"][field] == value


    @pytest.mark.parametrize(
        "field, value", [("email", helper.generate_random_email()),
                         ("name", helper.generate_random_string(7))]
    )

    @allure.title('Изменение данных пользователя без авторизации')
    def test_update_user_data_without_authorization(self, field, value):
        url = "https://stellarburgers.nomoreparties.site/api/auth/user"
        payload = {
            field: value
        }
        with allure.step("Отправка запроса на обновление данных без токена"):
            response = requests.patch(url, json=payload)
        with allure.step("Проверка статуса ответа и сообщения"):
            assert response.status_code == 401
            assert response.json()["success"] == False
            assert response.json()["message"] == "You should be authorised"