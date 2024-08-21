from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

main_page_locators = MainPageLocators()


class MainPage(BasePage):
    @allure.step('Пролистать страницу до вопроса в разделе "Частые вопросы"')
    def scroll_to_faq(self, question_key):
        locator = MainPageLocators.QUESTIONS[question_key]
        question = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(question)
        )

    @allure.step('Пролистать страницу до кнопки "Заказать"')
    def scroll_to_order_button(self):
        order_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(tuple(MainPageLocators.ROADMAP_ORDER_BUTTON)))
        self.driver.execute_script("arguments[0].scrollIntoView();", order_button)


    @allure.step('Раскрыть вопрос')
    def open_question(self, question_locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(tuple(main_page_locators.QUESTIONS[question_locator]))
        )
        self.driver.find_element(*main_page_locators.QUESTIONS[question_locator]).click()

    @allure.step('Получить текст ответа на вопрос')
    def get_answer_text_from_faq(self, answer_locator):
        return self.driver.find_element(*main_page_locators.ANSWERS[answer_locator]).text

    @allure.step('Нажать на кнопку "Заказать"')
    def click_to_order_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(tuple(MainPageLocators.ROADMAP_ORDER_BUTTON))
        )
        self.driver.find_element(*main_page_locators.ROADMAP_ORDER_BUTTON).click()

    @allure.step('Проверить заголовок на лендинге с самокатом')
    def check_url_on_scooter_landing_page(self):
        self.driver.find_element(*main_page_locators.MAIN_PAGE_HEADER)