from locators.locators_main_page_switch import MainPageSwitchLocators
from pages.base_page import BasePage
import allure
from data import Url

class MainPageSwitchPage(BasePage):
    @allure.step('Нажать на лого Самокат')
    def click_on_logo_scooter(self):
        self.click_on_element(MainPageSwitchLocators.logo_header_scooter)

    @allure.step('Нажать на лого Яндекс')
    def click_on_logo_yandex(self):
        self.click_on_element(MainPageSwitchLocators.logo_header_yandex)

    @allure.step('Проверить URL Яндекс Самокат')
    def check_switch_scooter_page(self):
        self.cross_url(Url.scooter_main_page)

    @allure.step('Проверить URL Дзен')
    def check_switch_dzen_page(self):
        self.cross_url(Url.dzen_main_page)
