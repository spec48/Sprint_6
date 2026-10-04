import allure
import pytest
from ..data import ORDER_DATA_1_SET, ORDER_DATA_2_SET, popup_message
from  ..locators.main_page_locators import MainPageLocators
from Sprint_6.urls import *


class TestOrderPage:

    @allure.title('Создание заказа')
    @allure.description('Тест проверяет появление всплывающего окна с сообщением об успешном создании заказа')
    @pytest.mark.parametrize('locator, order_data',
                             [
                                 [MainPageLocators.UP_BUTTON_ORDER, ORDER_DATA_1_SET],
                                 [MainPageLocators.DOWN_BUTTON_ORDER, ORDER_DATA_2_SET],
                             ]
                             )
    def test_create_order_page(self, order_page, locator, order_data):
        order_page.go_url(MAIN_PAGE_URL)
        order_page.scroll_to_element(locator)
        order_page.click_element(locator)
        order_page.fill_out_the_order_pages(order_data)
        assert popup_message in order_page.get_text_from_popup_window(), ('Всплывающее окно с сообщением об успешном'
                                                                           ' создании заказа не появилось.')
