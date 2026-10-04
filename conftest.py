import pytest
from selenium import webdriver
import allure
from .page_objects.main_page import MainPage
from .page_objects.order_page import OrderPage


@pytest.fixture(scope="function")
@allure.title("Подготовка веб драйвера")
def driver():
    with allure.step('Создание объекта веб драйвера Chrome'):
        driver = webdriver.Chrome()
    yield driver
    with allure.step('Закрытие веб драйвера'):
        driver.quit()

@pytest.fixture(scope="function")
def main_page(driver):
    page = MainPage(driver)
    return page

@pytest.fixture(scope="function")
def order_page(driver):
    page = OrderPage(driver)
    return page