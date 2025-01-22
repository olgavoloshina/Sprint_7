import allure
import requests
from helpers import generate_random_string


@allure.step(f'Дергаем ручку v1/courier')
def post_create_courier(body: dict):
    return requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=body)


@allure.step(f'Дергаем ручку v1/courier/login')
def post_login_courier(body: dict):
    return requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=body)


@allure.step(f'Дергаем ручку v1/orders')
def post_create_order(metro: int, rent: int, colors: list):
    body = {
        "firstName": generate_random_string(10),
        "lastName": generate_random_string(10),
        "address": generate_random_string(10),
        "metroStation": metro,
        "phone": "+7 800 355 35 35",
        "rentTime": rent,
        "deliveryDate": "2020-06-06",
        "comment": "agile, scrum? fy, IM RUSSIAN",
        "color": colors
    }

    return requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=body)


@allure.step(f'Дергаем ручку v1/orders')
def get_orders():
    return requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
