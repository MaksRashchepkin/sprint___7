from locators.locators_page_order_scooter import PageOrderLocators
from pages.base_page import BasePage
import allure

class OrderScooterPage(BasePage):
    @allure.step('Заполнить поле "Имя"')
    def enter_name(self, name):
        self.add_text_to_element(PageOrderLocators.name_field, name)

    @allure.step('Заполнить поле "Фамилия"')
    def enter_surname(self, surname):
        self.add_text_to_element(PageOrderLocators.surname_field, surname)

    @allure.step('Заполнить поле "Адрес: куда привезти заказ"')
    def enter_address(self, address):
        self.add_text_to_element(PageOrderLocators.address_field, address)

    @allure.step('Выбрать станцию метро')
    def enter_metro(self, metro):
        locator_metro = PageOrderLocators.metro_locator(metro)
        self.add_text_to_element(PageOrderLocators.metro_field, metro)
        self.click_on_element(locator_metro)

    @allure.step('Заполнить поле "Телефон: на него позвонит курьер"')
    def enter_telephone(self, telephone):
        self.add_text_to_element(PageOrderLocators.telephone_filed, telephone)

    @allure.step('Нажать на кнопку "Далее"')
    def click_on_button_enter_first_page_order(self):
        self.click_on_element(PageOrderLocators.button_further)

    @allure.step('Выбрать дату доставки')
    def enter_when_scooter(self, when_scooter):
        self.add_text_to_element(PageOrderLocators.when_need_scooter_field, when_scooter)

    @allure.step('Выбрать срок аренды')
    def enter_the_rental_period(self, the_rental_period):
        locator_rental_period = PageOrderLocators.rent_time_locator(the_rental_period)
        self.click_on_element(PageOrderLocators.drop_dawn_rental)
        self.click_on_element(locator_rental_period)

    @allure.step('Выбрать цвет')
    def enter_when_check_box_colour(self, check_box_colour):
        locator_check_box = PageOrderLocators.check_box_colour_locator(check_box_colour)
        self.click_on_element(locator_check_box)

    @allure.step('Заполнить поле "Комментарий для курьера"')
    def enter_comment(self, comment):
        self.add_text_to_element(PageOrderLocators.comment, comment)

    @allure.step('Нажать на кнопку "Заказать"')
    def click_on_button_order(self):
        self.click_on_element(PageOrderLocators.button_order)

    @allure.step('Всплывающее окно "Хотите оформить заказ?"')
    def check_screen_want_set_order(self):
        self.find_element_with_wait(PageOrderLocators.screen_want_set_order)

    @allure.step('Нажать на кнопку "Да"')
    def click_on_button_yes_or_not(self):
        self.click_on_element(PageOrderLocators.button_yes)

    @allure.step('Всплывающее окно "Заказ оформлен"')
    def check_success_order(self):
        self.find_element(PageOrderLocators.screen_order_complete)

    @allure.step('Во всплывающем окне "Заказ оформлен" отображается фраза "Номер заказа: "')
    def check_text_order_complete(self):
        return self.get_text(PageOrderLocators.text_order_complete)

    def create_order(self, name, surname, address, metro, telephone, when_scooter, the_rental_period, check_box_colour, comment):
        self.enter_name(name)
        self.enter_surname(surname)
        self.enter_address(address)
        self.enter_metro(metro)
        self.enter_telephone(telephone)
        self.click_on_button_enter_first_page_order()
        self.enter_when_scooter(when_scooter)
        self.enter_when_check_box_colour(check_box_colour)
        self.enter_the_rental_period(the_rental_period)
        self.enter_comment(comment)
        self.click_on_button_order()
        self.check_screen_want_set_order()
        self.click_on_button_yes_or_not()
        self.check_success_order()
