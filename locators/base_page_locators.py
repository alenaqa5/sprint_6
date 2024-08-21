from selenium.webdriver.common.by import By


class BasePageLocators:
    COOKIE_AGREEMENT = [By.ID, "rcc-confirm-button"]
    HEADER_ORDER_BUTTON = [By.XPATH, "//button[contains(@class,'Button_Button') and contains(text(),'Заказать')]"]
    YANDEX_LOGO = [By.XPATH, "//a[contains(@href,'//yandex.ru') and contains(@class,'Header_Logo')]"]
    SCOOTER_LOGO = [By.XPATH, "//a[contains(@href,'/') and contains(@class,'Header_LogoScooter')]"]
