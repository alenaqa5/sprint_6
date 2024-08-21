from selenium.webdriver.common.by import By


class OrderScooterLocators:
    NAME = [By.XPATH, "//input[contains(@placeholder,'* Имя')]"]
    SURNAME = [By.XPATH, "//input[contains(@placeholder,'* Фамилия')]"]
    ADDRESS = [By.XPATH, "//input[contains(@placeholder,'* Адрес: куда привезти заказ')]"]
    METRO_STATION_FIELD = [By.XPATH, "//input[contains(@placeholder,'* Станция метро')]"]
    METRO_STATION = [By.XPATH, "//li[contains(@class, 'select-search__row')]//button[contains(@class, 'Order_SelectOption')]//div[contains(@class,'Order_Text') and contains(text(),'Бульвар Рокоссовского')]"]
    PHONE_NUMBER = [By.XPATH, "//input[contains(@placeholder,'* Телефон: на него позвонит курьер')]"]
    CONTINUE = [By.XPATH, "//button[contains(text(),'Далее')]"]
    WHEN_TO_DELIVER_SCOOTER = [By.XPATH, "//input[contains(@placeholder,'* Когда привезти самокат')]"]
    WHEN_TO_DELIVER_SCOOTER_CALENDAR = [By.XPATH, "//*[contains(@class,'react-datepicker__day react-datepicker__day--001') and contains(@aria-label,'Choose воскресенье, 1-е сентября 2024 г.')]"]
    DURATION_OF_RENT = [By.XPATH, "//*[contains(@class,'Dropdown-placeholder')]"]
    DURATION_OF_RENT_DAY = [By.XPATH, "//*[contains(@class,'Dropdown-option') and contains(text(),'сутки')]"]
    DURATION_OF_RENT_TWO_DAYS = [By.XPATH, "//*[contains(@class,'Dropdown-option') and contains(text(),'двое суток')]"]
    COLOR_OF_SCOOTER_IS_BLACK = [By.XPATH, "//input[@id='black']"]
    COMMENT_FOR_COURIER = [By.XPATH, "//input[contains(@placeholder,'Комментарий для курьера')]"]
    ORDER_BUTTON = [By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[contains(text(), 'Заказать')]"]
    CONFIRM_ORDER_TITLE = [By.XPATH, "//div[contains(@class, 'Order_ModalHeader')] [contains(text(), 'Хотите оформить заказ?')]"]
    CONFIRM_CREATE_ORDER = [By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[contains(text(), 'Да')]"]
    CONFIRMATION_OF_CREATED_ORDER_TITLE = [By.XPATH, "//div[contains(@class, 'Order_Modal') and contains(text(), 'Заказ оформлен')]"]
    CHECK_STATUS = [By.XPATH, "//div[contains(@class, 'Order_NextButton')]//button[contains(@class,'Button_Button')]"]