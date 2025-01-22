import allure
from handlers.handlers import get_orders


@allure.epic("HTTP")
@allure.feature("v1/orders")
@allure.suite('Проверка ручку получения заказов')
class TestGetOrders:

    @allure.title(f'Получаем все заказы')
    def test_get_orders(
            self,
    ):
        response = get_orders().json()
        expected_res = {
            'id': 383,
            'courierId': None,
            'firstName': 'Наталья',
            'lastName': 'Губанова',
            'address': 'Москва',
            'metroStation': '3',
            'phone': '+79779816818',
            'rentTime': 5,
            'deliveryDate': '2021-10-21T21:00:00.000Z',
            'track': 705638,
            'color': ['BLACK'],
            'comment': '',
            'createdAt': '2021-10-01T11:05:57.834Z',
            'updatedAt': '2021-10-01T11:05:57.834Z',
            'status': 0
        }
        assert response["orders"][0] == expected_res
