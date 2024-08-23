import allure
import data
from pages.order_scooter_form import OrderSooter
from pages.main_page import MainPage


class TestOrderScooter:
    @allure.title('Создание заказа через кнопку "Заказать" на странице лендинга')
    @allure.description('Данный сценарий содержит процесс заполнения формы, создания заказа, и проверки редиректов по логотипам.')
    def test_create_order_for_scooter_by_order_button_on_main_page_all_fields_filed(self, driver):
        order_form = OrderSooter(driver)
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.scroll_to_order_button()
        main_page.click_to_order_button()
        order_form.fill_fields_contact_data(data.client_1['Имя'], data.client_1['Фамилия'], data.client_1['Адрес'], data.client_1['Номер телефона'])
        order_form.proceed_to_scooter_details()
        order_form.fill_rent_details()
        order_form.choose_scooter_color()
        order_form.input_comment_for_courier(data.client_1['Коммент курьеру'])
        order_form.order_scooter()
        order_form.confirm_ordering_scooter()
        order_form.check_order_created()
        order_form.close_popup_with_success_message()
        order_form.click_on_scooter_logo()
        main_page.check_url_on_scooter_landing_page()
        main_page.click_on_yandex_logo()
        main_page.check_new_tab_url('https://dzen.ru/?yredirect=true')

    @allure.title('Создание заказа через кнопку "Заказать" в заголовке лендинга')
    @allure.description('Заполняем форму, создаем заказ, проверяем редиректы. Точка входа: кнопка "Заказать" в заголовке лендинга.')
    def test_create_order_for_scooter_by_header_order_button_only_required_fields_filled(self, driver):
        order_form = OrderSooter(driver)
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.click_on_header_order_button()
        order_form.fill_fields_contact_data(data.client_2['Имя'], data.client_2['Фамилия'], data.client_2['Адрес'],
                                            data.client_2['Номер телефона'])
        order_form.proceed_to_scooter_details()
        order_form.fill_rent_details()
        order_form.order_scooter()
        order_form.confirm_ordering_scooter()
        order_form.check_order_created()
        order_form.close_popup_with_success_message()
        order_form.click_on_scooter_logo()
        main_page.check_url_on_scooter_landing_page()
        main_page.click_on_yandex_logo()
        main_page.check_new_tab_url('https://dzen.ru/?yredirect=true')

