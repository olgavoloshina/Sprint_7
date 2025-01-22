import allure
from handlers.handlers import post_login_courier


@allure.epic("HTTP")
@allure.feature("v1/courier/login")
@allure.suite('Проверка ручку логина курьера')
class TestLoginCourier:

    @allure.title(f'Проверяем логин зарегестированного курьера')
    def test_login_courier(
            self,
            register_new_courier_and_return_login_password: dict
    ):
        body = {
            "login": register_new_courier_and_return_login_password["login"],
            "password": register_new_courier_and_return_login_password["password"]
        }
        response = post_login_courier(body=body)

        assert response.ok
        assert "id" in response.json()

    @allure.title(f'Проверяем ошибку логина зарегестированного курьера, с пустым логином')
    def test_error_login_courier_with_null_login(
            self,
            register_new_courier_and_return_login_password: dict
    ):
        body = {
            "login": '',
            "password": register_new_courier_and_return_login_password["password"],
        }
        response = post_login_courier(body=body).json()

        assert response["message"] == 'Недостаточно данных для входа'

    @allure.title(f'Проверяем ошибку логина зарегестированного курьера, с пустым паролем')
    def test_error_login_courier_with_null_password(
            self,
            register_new_courier_and_return_login_password: dict
    ):
        body = {
            "login": register_new_courier_and_return_login_password["login"],
            "password": '',
        }
        response = post_login_courier(body=body).json()

        assert response["message"] == 'Недостаточно данных для входа'

    @allure.title(f'Проверяем ошибку логина для не зарегестированного курьера')
    def test_error_login_mot_register_courier(
            self,
            generate_and_return_login_password: dict
    ):
        body = {
            "login": generate_and_return_login_password["login"],
            "password": generate_and_return_login_password["password"]
        }
        response = post_login_courier(body=body).json()

        assert response["message"] == 'Учетная запись не найдена'

    @allure.title(f'Проверяем ошибку логина зарегестированного курьера с ошибкой в логине')
    def test_error_login_courier_with_incorrect_login(
            self,
            register_new_courier_and_return_login_password: dict
    ):
        body = {
            "login": register_new_courier_and_return_login_password["login"]+'test',
            "password": register_new_courier_and_return_login_password["password"]
        }
        response = post_login_courier(body=body).json()

        assert response["message"] == 'Учетная запись не найдена'

    @allure.title(f'Проверяем ошибку логина зарегестированного курьера с ошибкой в пароле')
    def test_error_login_courier_with_incorrect_password(
            self,
            register_new_courier_and_return_login_password: dict
    ):
        body = {
            "login": register_new_courier_and_return_login_password["login"],
            "password": register_new_courier_and_return_login_password["password"]+'test'
        }
        response = post_login_courier(body=body).json()

        assert response["message"] == 'Учетная запись не найдена'
