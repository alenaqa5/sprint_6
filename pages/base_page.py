import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def scroll_to_element(self, element) -> WebElement:
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))

    @allure.step('Проверить редирект на новую вкладку')
    def check_new_tab_url(self, expected_url):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be(expected_url))
        assert self.driver.current_url == expected_url

