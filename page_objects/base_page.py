from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 3
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def fill_out_the_field(self, field, value):
        self.find_element(field).send_keys(value)

    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text

    def switch_to_another_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def format_locator(self, selen_locator, number):
        method, locator = selen_locator
        locator = locator.format(number)
        return method, locator
