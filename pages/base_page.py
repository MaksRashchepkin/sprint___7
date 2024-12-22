from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_the_page(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        self.driver.find_element(*locator)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        self.find_element_with_wait(locator).click()

    def get_text(self, locator):
        return self.find_element_with_wait(locator).text

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def format_locators(self, locator_question, index):
        method, locator = locator_question
        locator = locator.format(index)
        return (method, locator)

    def tab_switch(self, driver):
        self.driver.switch_to.window(driver.window_handles[1])

    def cross_url(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))

    def get_current_url(self):
        return self.driver.current_url
