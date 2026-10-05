import allure
from selenium.common import TimeoutException
from ..urls import base_url, order_page_url
from ..locators.main_page_locators import MainPageLocators
from ..locators.transition_locators import *


class TestTransitionByUrls:

    @allure.title('Проверка перехода на главную страницу "Самоката"')
    @allure.description('Тест проверяет, что если нажать на логотип "Самоката", попадёшь на главную страницу "Самоката"')
    @allure.step('Клик на логотип "Самоката" и переход на главную страницу')
    def test_check_go_to_main_page_scooter(self, order_page):
        order_page.go_url(order_page_url)
        order_page.click_element(MainPageLocators.SCOOTER_LOGO)
        assert order_page.find_element(MainPageLocators.SCOOTER_IMAGE).is_displayed()

    @allure.title('Проверка перехода на главную страницу "Дзена"')
    @allure.description('Тест проверяет, что если нажать на логотип Яндекса, в новом окне через редирект откроется'
                        ' главная страница Дзена')
    @allure.step('Клик на логотип Яндекса и переход на главную страницу Дзена')
    def test_check_go_to_main_page_dzen(self, main_page):
        main_page.go_url(base_url)
        main_page.click_element(MainPageLocators.YANDEX_LOGO)
        main_page.switch_to_another_window()
        assert main_page.find_element(MainPageDzenLocator.DZEN_LOGO).is_displayed()
