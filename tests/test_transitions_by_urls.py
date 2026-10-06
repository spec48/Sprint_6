import allure
import pytest
from ..urls import base_url, order_page_url
from ..locators.main_page_locators import MainPageLocators
from ..locators.transition_locators import *


class TestTransitionByUrls:

    @allure.title('Проверка перехода на главную страницу "Самоката"')
    @allure.description('Тест проверяет, что если нажать на логотип "Самоката", попадёшь на главную страницу "Самоката"')
    @allure.step('Клик на логотип "Самоката" и переход на главную страницу')
    @pytest.mark.parametrize('locator_scooter, locator_main_page',
                             [
                                 [MainPageLocators.SCOOTER_LOGO, MainPageLocators.SCOOTER_IMAGE],
                             ]
                             )
    def test_check_go_to_main_page_scooter(self, order_page, locator_scooter, locator_main_page):
        order_page.go_url(order_page_url)
        order_page.click_element(locator_scooter)
        assert order_page.find_element(locator_main_page).is_displayed()

    @allure.title('Проверка перехода на главную страницу "Дзена"')
    @allure.description('Тест проверяет, что если нажать на логотип Яндекса, в новом окне через редирект откроется'
                        ' главная страница Дзена')
    @allure.step('Клик на логотип Яндекса и переход на главную страницу Дзена')
    @pytest.mark.parametrize('locator_yandex, locator_dzen',
                             [
                                 [MainPageLocators.YANDEX_LOGO, MainPageDzenLocator.DZEN_LOGO],
                             ]
                             )
    def test_check_go_to_main_page_dzen(self, main_page, locator_yandex, locator_dzen):
        main_page.go_url(base_url)
        main_page.click_element(locator_yandex)
        main_page.switch_to_another_window()
        assert main_page.find_element(locator_dzen).is_displayed()
