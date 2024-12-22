from selenium.webdriver.common.by import By

class PageOrderLocators:
    name_field = (By.XPATH, "//input[@placeholder= '* Имя']")
    surname_field = (By.XPATH, "//input[@placeholder= '* Фамилия']")
    address_field = (By.XPATH, "//input[@placeholder= '* Адрес: куда привезти заказ']")
    metro_field = (By.XPATH, "//input[@placeholder= '* Станция метро']")
    telephone_filed = (By.XPATH, "//input[@placeholder= '* Телефон: на него позвонит курьер']")
    button_further = (By.XPATH, "//button[text() = 'Далее']")
    when_need_scooter_field = (By.XPATH, "//input[@placeholder= '* Когда привезти самокат']")
    drop_dawn_rental = (By.XPATH, "//*[text() = '* Срок аренды']")
    comment = (By.XPATH, "//input[@placeholder= 'Комментарий для курьера']")
    button_order = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    screen_want_set_order = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='Хотите оформить заказ?']")
    button_yes = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text() = 'Да']")
    screen_order_complete = (By.XPATH, "//div[@class='Order_Modal__YZ-d3']")
    text_order_complete = (By.XPATH, "//div[@class='Order_Text__2broi']")

    @staticmethod
    def metro_locator(metro):
        return By.XPATH, f"//*[contains(text(), '{metro[0]}')]"

    @staticmethod
    def check_box_colour_locator(check_box_colour):
        return By.ID, f"{check_box_colour[0]}"

    @staticmethod
    def rent_time_locator(the_rental_period):
        return By.XPATH, f"//div[text() = '{the_rental_period[0]}']"
