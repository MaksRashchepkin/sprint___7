import allure
from conftest import driver, cookies
from pages.main_page_switch import MainPageSwitchPage
from data import Url

class TestMainPageLogo:
    @allure.title('Клик на лого Самокат в шапке страницы открывает главную страницу "Яндекс Самокат"')
    def test_scooter_logo(self, driver, cookies):
        main_page_logo = MainPageSwitchPage(driver)
        main_page_logo.click_on_logo_scooter()
        main_page_logo.check_switch_scooter_page()
        assert main_page_logo.get_current_url() == Url.scooter_main_page

    @allure.title('Клик на лого Яндекс в шапке страницы открывает главную страницу "Дзен"')
    def test_dzen_logo(self, driver, cookies):
        main_page_logo = MainPageSwitchPage(driver)
        main_page_logo.click_on_logo_yandex()
        main_page_logo.tab_switch(driver)
        main_page_logo.check_switch_dzen_page()
        assert main_page_logo.get_current_url() == Url.dzen_main_page
