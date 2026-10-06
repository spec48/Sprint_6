import allure
from selenium.webdriver import Keys
from .base_page import BasePage
from  ..locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Заполнение первой страницы заказа')
    def fill_out_the_first_page(self, order_data):
        self.click_element(OrderPageLocators.FIELD_NAME)
        self.fill_out_the_field(OrderPageLocators.FIELD_NAME, order_data['name'])
        self.fill_out_the_field(OrderPageLocators.FIELD_LAST_NAME, order_data['last_name'])
        self.fill_out_the_field(OrderPageLocators.FIELD_ADDRESS, order_data['address'])
        self.click_element(OrderPageLocators.FIELD_METRO)
        locator_metro_formatted = self.format_locator(OrderPageLocators.METRO, order_data['metro'])
        self.click_element(locator_metro_formatted)
        self.fill_out_the_field(OrderPageLocators.FIELD_PHONE, order_data['phone'])
        self.click_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнение второй страницы заказа')
    def fill_out_the_second_page(self, order_data):
        self.click_element(OrderPageLocators.FIELD_DELIVERY_DATE)
        self.fill_out_the_field(OrderPageLocators.FIELD_DELIVERY_DATE, order_data['date'])
        self.fill_out_the_field(OrderPageLocators.FIELD_DELIVERY_DATE, Keys.ENTER)
        self.click_element(OrderPageLocators.FIELD_RENTAL_PERIOD)
        locator_period_formatted = self.format_locator(OrderPageLocators.RENTA_PERIOD, order_data['renta_period'])
        self.click_element(locator_period_formatted)
        locator_color_formatted = self.format_locator(OrderPageLocators.COLOR, order_data['color'])
        self.click_element(locator_color_formatted)
        self.fill_out_the_field(OrderPageLocators.COMMENT, order_data['comment'])

    @allure.step('Заполнение страниц заказа')
    def fill_out_the_order_pages(self, order_data):
        self.fill_out_the_first_page(order_data)
        self.fill_out_the_second_page(order_data)
        with allure.step('Клик на кнопку "Заказать"'):
            self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Получение сообщения из всплывающего окна')
    def get_text_from_popup_window(self):
        return self.get_text_from_element(OrderPageLocators.POPUP_WINDOW)
