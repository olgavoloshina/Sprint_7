from typing import Optional
import allure
import pytest
from handlers.handlers import post_create_order


@allure.epic("HTTP")
@allure.feature("v1/orders")
@allure.suite('Проверка ручку создание заказа')
class TestCreateOrder:

    @pytest.mark.parametrize("metro,rent,colors", [
        (4, 5, ["BLACK"]),
        (2, 1, ["GREY"]),
        (1, 3, []),
        (3, 7, ["BLACK", "GREY"]),
        (6, 2, None)
    ]
                             )
    @allure.title(f'Создаем заказ с несколькими данными')
    def test_create_order(
            self,
            metro: int,
            rent: int,
            colors: Optional[list]
    ):
        response = post_create_order(metro=metro, rent=rent, colors=colors).json()

        assert "track" in response
