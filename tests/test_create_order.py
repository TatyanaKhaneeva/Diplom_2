import requests
import allure

class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_authorization(self, create_and_login_user, ingredients):
        url = "https://stellarburgers.nomoreparties.site/api/orders"
        token = create_and_login_user['accessToken']
        ingredient_ids = [ingredients[0]["_id"], ingredients[1]["_id"]]
        payload = {"ingredients": ingredient_ids}
        headers = {"Authorization": token}
        with allure.step("Отправка запроса на создание заказа с токеном"):
            response = requests.post(url, json=payload, headers=headers)
        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 200
            assert response.json()["success"] == True



    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_authorization(self, ingredients):
        url = "https://stellarburgers.nomoreparties.site/api/orders"
        ingredient_ids = [ingredients[0]["_id"], ingredients[1]["_id"]]
        payload = {"ingredients": ingredient_ids}

        with allure.step("Отправка запроса на создание заказа без авторизации"):
            response = requests.post(url, json=payload)

        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 200
            assert response.json()["success"] == True



    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, create_and_login_user):
        url = "https://stellarburgers.nomoreparties.site/api/orders"
        token = create_and_login_user['accessToken']

        payload = {"ingredients": []}
        headers = {"Authorization": token}
        with allure.step("Отправка запроса на создание заказа с токеном"):
            response = requests.post(url, json=payload, headers=headers)
        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 400
            assert response.json()["success"] == False
            assert response.json()["message"] == "Ingredient ids must be provided"



    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_ingredient_hash(self, create_and_login_user):
        url = "https://stellarburgers.nomoreparties.site/api/orders"
        token = create_and_login_user['accessToken']
        payload = {"ingredients": ["chbvklsdfhvd", "gbfncjknv"]}
        headers = {"Authorization": token}
        with allure.step("Отправка запроса на создание заказа с токеном"):
            response = requests.post(url, json=payload, headers=headers)
        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 500
