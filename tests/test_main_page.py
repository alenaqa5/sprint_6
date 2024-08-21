import pytest
from pages.main_page import MainPage
import allure


class TestMainPage:
    @allure.title('Раскрытие вопросов в разделе "Вопросы о важном"')
    @allure.description('В разделе "Вопросы о важном" есть список вопросов с ответами, проверяем содержание текста в ответах и функционал раскрытия вопросов')
    @pytest.mark.parametrize("question_locator, answer_locator, expected_answer", [
        ("HOW_MUCH_IT_COST", "HOW_MUCH_IT_COST_ANSWER", "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        ("FEW_SCOOTERS", "FEW_SCOOTERS_ANSWER", "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        ("RENT_TIME", "RENT_TIME_ANSWER", "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        ("ORDER_SCOOTER_FOR_TODAY", "ORDER_SCOOTER_FOR_TODAY_ANSWER", "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        ("PROLONGE_AND_RETURN_SCOOTER", "PROLONGE_AND_RETURN_SCOOTER_ANSWER", "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        ("CHARGER_FOR_SCOOTER", "CHARGER_FOR_SCOOTER_ANSWER", "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        ("AVALABILLITY_OF_CANCELATION", "AVALABILLITY_OF_CANCELATION_ANSWER", "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        ("SUBURBS_OF_MOSCOW", "SUBURBS_OF_MOSCOW_ANSWER", "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
    ])
    def test_check_text_from_expanded_question_faq(self, driver, question_locator, answer_locator, expected_answer):
        faq_page = MainPage(driver)
        faq_page.accept_cookie()
        faq_page.scroll_to_faq(question_locator)
        faq_page.open_question(question_locator)
        answer_text = faq_page.get_answer_text_from_faq(answer_locator)
        assert answer_text == expected_answer

