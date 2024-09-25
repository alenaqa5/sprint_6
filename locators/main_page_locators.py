from selenium.webdriver.common.by import By


class MainPageLocators:
    FAQ_HEADER = [By.XPATH, "//*[text()='Вопросы о важном']"]
    ROADMAP_ORDER_BUTTON = [By.XPATH, "//*[contains(@class,'Home_Finish')]//button[contains(@class,'Button_Middle') and contains(text(),'Заказать')]"]
    QUESTIONS = {
        "HOW_MUCH_IT_COST": [By.XPATH, "//*[contains(text(),'Сколько это стоит? И как оплатить?') and contains(@class,'accordion__button')]"],
        "FEW_SCOOTERS": [By.XPATH, "//*[contains(text(),'Хочу сразу несколько самокатов! Так можно?') and contains(@class,'accordion__button')]"],
        "RENT_TIME": [By.XPATH, "//*[contains(text(),'Как рассчитывается время аренды?') and contains(@class,'accordion__button')]"],
        "ORDER_SCOOTER_FOR_TODAY": [By.XPATH, "//*[contains(text(),'Можно ли заказать самокат прямо на сегодня?') and contains(@class,'accordion__button')]"],
        "PROLONGE_AND_RETURN_SCOOTER": [By.XPATH, "//*[contains(text(),'Можно ли продлить заказ или вернуть самокат раньше?') and contains(@class,'accordion__button')]"],
        "CHARGER_FOR_SCOOTER": [By.XPATH, "//*[contains(text(),'Вы привозите зарядку вместе с самокатом?') and contains(@class,'accordion__button')]"],
        "AVALABILLITY_OF_CANCELATION": [By.XPATH, "//*[contains(text(),'Можно ли отменить заказ?') and contains(@class,'accordion__button')]"],
        "SUBURBS_OF_MOSCOW": [By.XPATH, "//*[contains(text(),'Я жизу за МКАДом, привезёте?') and contains(@class,'accordion__button')]"]
    }
    ANSWERS = {
        "HOW_MUCH_IT_COST_ANSWER": [By.XPATH, "//p[contains(text(),'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')]"],
        "FEW_SCOOTERS_ANSWER": [By.XPATH, "//p[contains(text(),'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')]"],
        "RENT_TIME_ANSWER": [By.XPATH, "//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')]"],
        "ORDER_SCOOTER_FOR_TODAY_ANSWER": [By.XPATH, "//p[contains(text(),'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')]"],
        "PROLONGE_AND_RETURN_SCOOTER_ANSWER": [By.XPATH, "//p[contains(text(),'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')]"],
        "CHARGER_FOR_SCOOTER_ANSWER": [By.XPATH, "//p[contains(text(),'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')]"],
        "AVALABILLITY_OF_CANCELATION_ANSWER": [By.XPATH, "//p[contains(text(),'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')]"],
        "SUBURBS_OF_MOSCOW_ANSWER": [By.XPATH, "//p[contains(text(),'Да, обязательно. Всем самокатов! И Москве, и Московской области.')]"]
    }
    MAIN_PAGE_HEADER = [By.XPATH, "//*[contains(@class,'Home_Header')and contains(text(),'Самокат ')]"]
    COOKIE_AGREEMENT = [By.ID, "rcc-confirm-button"]
    HEADER_ORDER_BUTTON = [By.XPATH, "//button[contains(@class,'Button_Button') and contains(text(),'Заказать')]"]
    YANDEX_LOGO = [By.XPATH, "//a[contains(@href,'//yandex.ru') and contains(@class,'Header_Logo')]"]


