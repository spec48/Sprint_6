import allure
from .base_page import BasePage
from ..locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Клик на вопрос в разделе "Вопросы о важном"')
    def click_to_question(self, number):
        locator_question_formatted = self.format_locator(MainPageLocators.QUESTION_LOCATOR, number)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_FOR_SCROLL)
        self.click_element(locator_question_formatted)

    @allure.step('Получение ответа на вопрос"')
    def get_answer_text(self, number):
        locator_answer_formatted = self.format_locator(MainPageLocators.ANSWER_LOCATOR, number)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_FOR_SCROLL)
        return self.get_text_from_element(locator_answer_formatted)

    @allure.step('Проверка ответа')
    def check_answer(self, number, answer_text):
        self.click_to_question(number)
        return self.get_answer_text(number) == answer_text
