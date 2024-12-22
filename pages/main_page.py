from locators.locators_main_page import MainPageLocators
from pages.base_page import BasePage
import allure

class MainPage(BasePage):
    @allure.step('Получить текст ответа на вопрос')
    def get_text_assert(self, number):
        locator_question_to_click_formated = self.format_locators(MainPageLocators.question, number)
        locator_question_text_formated = self.format_locators(MainPageLocators.answer, number)
        self.scroll_to_element(MainPageLocators.last_question)
        self.click_on_element(locator_question_to_click_formated)
        return self.get_text(locator_question_text_formated)

    @allure.step('Нажать на кнопку "Заказать" в хедере')
    def click_header_order_button(self):
        self.click_on_element(MainPageLocators.header_order_button)

    @allure.step('Нажать на кнопку "Заказать" в середине страницы')
    def click_middle_order_button(self):
        self.click_on_element(MainPageLocators.page_order_button)