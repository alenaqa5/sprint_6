from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

main_page_locators = MainPageLocators()


class MainPage(BasePage):
    @allure.step('Пролистать страницу до вопроса в разделе "Частые вопросы"')
    def scroll_to_faq(self, question_key):
        locator = MainPageLocators.QUESTIONS[question_key]
        question = self.wait_and_find_element(locator)
        self.scroll_to_element(question)

    @allure.step('Пролистать страницу до кнопки "Заказать"')
    def scroll_to_order_button(self):
        order_button = self.wait_and_find_element(MainPageLocators.ROADMAP_ORDER_BUTTON)
        self.scroll_to_element(order_button)

    @allure.step('Раскрыть вопрос')
    def open_question(self, question_locator):
        question = self.wait_and_find_element(main_page_locators.QUESTIONS[question_locator])
        self.scroll_to_element(question)
        question.click()

    @allure.step('Получить текст ответа на вопрос')
    def get_answer_text_from_faq(self, answer_locator):
        return self.wait_and_find_element(main_page_locators.ANSWERS[answer_locator]).text

    @allure.step('Нажать на кнопку "Заказать"')
    def click_to_order_button(self):
        self.wait_and_find_element(main_page_locators.ROADMAP_ORDER_BUTTON).click()

    @allure.step('Проверить заголовок на лендинге с самокатом')
    def check_url_on_scooter_landing_page(self):
        self.wait_and_find_element(main_page_locators.MAIN_PAGE_HEADER)

    @allure.step('Принять куки')
    def accept_cookie(self):
        self.wait_and_find_element(main_page_locators.COOKIE_AGREEMENT).click()

    @allure.step('Нажать на кнопку "заказать" в заголовке страницы')
    def click_on_header_order_button(self):
        self.wait_and_find_element(main_page_locators.HEADER_ORDER_BUTTON).click()

    @allure.step('Нажать на логотип яндекса')
    def click_on_yandex_logo(self):
        self.wait_and_find_element(main_page_locators.YANDEX_LOGO).click()
