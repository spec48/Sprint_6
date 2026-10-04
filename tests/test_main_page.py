import allure
import pytest
from ..data import answer_text_data
from ..urls import *


class TestMainPage:
    @allure.title('Проверка ответа на вопрос')
    @allure.description('При нажатии на вопрос в разделе "Вопросы о важном", открывается соответствующий текст')
    @pytest.mark.parametrize('number', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_check_questions_and_answers(self, main_page, number):
        main_page.go_url(MAIN_PAGE_URL)
        assert main_page.check_answer(number, answer_text_data[number]), ('Текст в разделе "Вопросы о важном"'
                                                                          ' отличается от текста в переменной '
                                                                          'answer_text_data в файле data.py')
