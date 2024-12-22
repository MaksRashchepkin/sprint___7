import allure
import pytest
from conftest import driver, cookies
from pages.page_order_scooter import OrderScooterPage
from pages.main_page import MainPage
from data import UserOne, UserTwo

class TestPageOrder:
    @allure.title('Проверка оформления заказа через кнопку "Заказать" в хедере')
    @pytest.mark.parametrize('name, surname, address, metro, telephone, when_scooter, the_rental_period, check_box_colour, comment', UserOne.user)
    def test_order_header_button(self, driver, cookies, name, surname, address, metro, telephone, when_scooter, the_rental_period, check_box_colour, comment):
        main_page = MainPage(driver)
        main_page.click_header_order_button()
        order_page = OrderScooterPage(driver)
        order_page.create_order(name, surname, address, metro, telephone, when_scooter, the_rental_period, check_box_colour, comment)
        assert 'Номер заказа: ' in order_page.check_text_order_complete()


    @allure.title('Проверка оформления заказа через кнопку "Заказать" в середине страницы')
    @pytest.mark.parametrize('name, surname, address, metro, telephone, when_scooter, the_rental_period, check_box_colour, comment', UserTwo.user)
    def test_order_middle_button(self, driver, cookies, name, surname, address, metro, telephone, when_scooter, the_rental_period, check_box_colour, comment):
        main_page = MainPage(driver)
        main_page.click_middle_order_button()
        order_page = OrderScooterPage(driver)
        order_page.create_order(name, surname, address, metro, telephone, when_scooter, the_rental_period, check_box_colour, comment)
        assert 'Номер заказа: ' in order_page.check_text_order_complete()
