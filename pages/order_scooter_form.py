from pages.base_page import BasePage
from locators.order_scooter_form_locators import OrderScooterLocators
import allure
order_scooter_locators = OrderScooterLocators()


class OrderSooter(BasePage):
    @allure.step('Ввести имя')
    def input_name(self, name):
        self.wait_and_find_element(order_scooter_locators.NAME).send_keys(name)

    @allure.step('Ввести фамилию')
    def input_surname(self, surname):
        self.wait_and_find_element(order_scooter_locators.SURNAME).send_keys(surname)

    @allure.step('Ввести адрес')
    def input_address(self, address):
        self.wait_and_find_element(order_scooter_locators.ADDRESS).send_keys(address)

    @allure.step('Ввести номер телефона')
    def input_phone_number(self, phone_number):
        self.wait_and_find_element(order_scooter_locators.PHONE_NUMBER).send_keys(phone_number)

    @allure.step('Выбрать дату для бронирования')
    def input_date_for_booking(self):
        self.wait_and_find_element(order_scooter_locators.WHEN_TO_DELIVER_SCOOTER).click()
        self.wait_and_find_element(order_scooter_locators.WHEN_TO_DELIVER_SCOOTER_CALENDAR).click()

    @allure.step('Открыть поле со станциями метро')
    def open_metro_station_field(self):
        metro_station_field = self.wait_and_find_element(order_scooter_locators.METRO_STATION_FIELD)
        metro_station_field.click()
        metro_station_field.send_keys('Бульвар Рокоссовского')

    @allure.step('Выбрать станцию метро')
    def choose_metro_station(self):
        self.wait_and_find_element(order_scooter_locators.METRO_STATION).click()

    @allure.step('Открыть поле для выбора длительности аренды')
    def open_duration_for_rent_field(self):
        self.wait_and_find_element(order_scooter_locators.DURATION_OF_RENT).click()

    @allure.step('Выбрать срок аренды')
    def choose_duration_for_rent(self, duration):
        self.wait_and_find_element(duration).click()

    @allure.step('Выбрать цвет самоката')
    def choose_scooter_color(self):
        self.wait_and_find_element(order_scooter_locators.COLOR_OF_SCOOTER_IS_BLACK).click()

    @allure.step('Ввести комментарий для курьера')
    def input_comment_for_courier(self, comment_for_courier):
        self.wait_and_find_element(order_scooter_locators.COMMENT_FOR_COURIER).send_keys(comment_for_courier)

    @allure.step('Перейти на следующий шаг формы')
    def proceed_to_scooter_details(self):
        self.wait_and_find_element(order_scooter_locators.CONTINUE).click()

    @allure.step('Нажать кнопку "Заказать"')
    def order_scooter(self):
        self.wait_and_find_element(order_scooter_locators.ORDER_BUTTON).click()

    @allure.step('Подтвердить создание заказа')
    def confirm_ordering_scooter(self):
        self.wait_and_find_element(order_scooter_locators.CONFIRM_CREATE_ORDER).click()

    @allure.step('Проверить текст в сообщении об успешном создании заказа')
    def check_order_created(self):
        return self.wait_and_find_element(order_scooter_locators.CONFIRMATION_OF_CREATED_ORDER_TITLE).text

    @allure.step('Закрыть попап об успешном создании заказа')
    def close_popup_with_success_message(self):
        self.wait_and_find_element(order_scooter_locators.CHECK_STATUS).click()

    @allure.step('Заполнить поля с контактными данными')
    def fill_fields_contact_data(self, name, surname, address, phone_number):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.open_metro_station_field()
        self.choose_metro_station()
        self.input_phone_number(phone_number)

    def fill_rent_details(self, ):
        self.input_date_for_booking()
        self.open_duration_for_rent_field()
        self.choose_duration_for_rent(order_scooter_locators.DURATION_OF_RENT_DAY)

    @allure.step('Нажать на логотип "самокат"')
    def click_on_scooter_logo(self):
        self.wait_and_find_element(order_scooter_locators.SCOOTER_LOGO).click()
