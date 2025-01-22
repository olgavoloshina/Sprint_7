import allure
import pytest
from handlers.handlers import post_create_courier


@allure.epic("HTTP")
@allure.feature("v1/courier")
@allure.suite('Проверка ручку создания курьера')
class TestCreatingCourier:

    @allure.title(f'Проверяем создание курьера')
    def test_register_new_courier(
            self,
            generate_and_return_login_password: dict
    ):
        body = {
            "login": generate_and_return_login_password["login"],
            "password": generate_and_return_login_password["password"],
            "firstName": generate_and_return_login_password["firstName"]
        }
        response = post_create_courier(body=body)

        assert response.ok
        assert response.json() == {'ok': True}

    @allure.title(f'Проверяем нельзя создать курьера дважды')
    def test_error_register_courier_twice(
            self,
            register_new_courier_and_return_login_password: dict
    ):
        body = {
            "login": register_new_courier_and_return_login_password["login"],
            "password": register_new_courier_and_return_login_password["password"],
            "firstName": register_new_courier_and_return_login_password["firstName"]
        }
        response = post_create_courier(body=body).json()

        assert response["message"] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title(f'Проверяем, что курьер не создается с пустым логином')
    def test_register_courier_with_null_login(
            self,
            generate_and_return_login_password: dict
    ):
        body = {
            "login": '',
            "password": generate_and_return_login_password["password"],
            "firstName": generate_and_return_login_password["firstName"]
        }
        response = post_create_courier(body=body).json()

        assert response["message"] == 'Недостаточно данных для создания учетной записи'

    @allure.title(f'Проверяем, что курьер не создается с пустым паролем')
    def test_register_courier_with_null_password(
            self,
            generate_and_return_login_password: dict
    ):
        body = {
            "login": generate_and_return_login_password["login"],
            "password": '',
            "firstName": generate_and_return_login_password["firstName"]
        }
        response = post_create_courier(body=body).json()

        assert response["message"] == 'Недостаточно данных для создания учетной записи'

    @pytest.mark.xfail
    @allure.title(f'Проверяем, что курьер не создается с пустым именем')
    def test_register_courier_with_null_first_name(
            self,
            generate_and_return_login_password: dict
    ):
        body = {
            "login": generate_and_return_login_password["login"],
            "password": generate_and_return_login_password["password"],
            "firstName": ''
        }
        response = post_create_courier(body=body).json()

        assert response["message"] == 'Недостаточно данных для создания учетной записи'
