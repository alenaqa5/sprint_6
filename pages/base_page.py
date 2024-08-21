from locators.base_page_locators import BasePageLocators
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_page_locators = BasePageLocators()


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажать на логотип яндекса')
    def click_on_yandex_logo(self):
        self.driver.find_element(*base_page_locators.YANDEX_LOGO).click()

    @allure.step('Проверить редирект на страницу яндекса')
    def check_new_tab_after_click_on_yandex_logo(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])
        expected_url = "https://dzen.ru/?yredirect=true"
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(expected_url)
        )
        assert self.driver.current_url == expected_url

    @allure.step('Нажать на логотип "самокат"')
    def click_on_scooter_logo(self):
        self.driver.find_element(*base_page_locators.SCOOTER_LOGO).click()

    @allure.step('Нажать на кнопку "заказать" в заголовке страницы')
    def click_on_header_order_button(self):
        self.driver.find_element(*base_page_locators.HEADER_ORDER_BUTTON).click()

    @allure.step('Принять куки')
    def accept_cookie(self):
        self.driver.find_element(*base_page_locators.COOKIE_AGREEMENT).click()
