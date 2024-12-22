import pytest
import allure
from conftest import driver, cookies
from pages.main_page import MainPage
from data import MainPageAnswers

class TestQuestionText:
    @allure.title('Проверка соответствия вопроса и ответа из выпадающего списка "Вопросы о важном"')
    @pytest.mark.parametrize('number, result', MainPageAnswers.answers)
    def test_main_page_question(self, driver, cookies, number, result):
        main_page = MainPage(driver)
        assert  main_page.get_text_assert(number) == result
