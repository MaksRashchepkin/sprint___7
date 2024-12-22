from selenium.webdriver.common.by import By

class MainPageLocators:
    question = (By.XPATH, "//*[@id='accordion__heading-{}']")
    answer = (By.XPATH, "//*[@id='accordion__panel-{}']")
    last_question = (By.XPATH, "//*[@id='accordion__heading-7']")
    header_order_button = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    page_order_button = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
    cookies_button = (By.ID, "rcc-confirm-button")
