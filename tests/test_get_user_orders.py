import requests
import allure

class TestGetUserOrders:

    @allure.title('Проверка получения заказов авторизованного пользователя')
    def test_get_user_orders(self, create_and_login_user):
        url = "https://stellarburgers.nomoreparties.site/api/orders"
        token = create_and_login_user['accessToken']
        headers = {"Authorization": token}
        with allure.step("Отправка запроса на получение заказов"):
            response = requests.get(url, headers=headers)
        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 200
            assert response.json()["success"] == True
            assert "orders" in response.json()


    @allure.title('Проверка получения заказов неавторизованного пользователя')
    def test_get_unauthorised_user_orders(self):
        url = "https://stellarburgers.nomoreparties.site/api/orders"

        with allure.step("Отправка запроса на получение заказов"):
            response = requests.get(url)
        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 401


