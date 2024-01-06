import allure

from pages.base_page import BasePage
from locators import MainPageLocators
from data import ConstantData


class MainPage(BasePage):
    """ Класс Главной страницы """

    @allure.step('Открываем Главную страницу')
    def open_main_page(self):
        # Открываем Главную страницу
        self.open_page(ConstantData.BASE_URL)
        # ждем загрузку Главной страницы
        self.wait_for_load_element(MainPageLocators.faq_list_of_questions)
        # кликаем согласие с куки
        self.click_accept_cookies_button()

    # Методы для работы с блоком "Вопросы о важном"
    @allure.step('Клик на вопрос с номером {index} - получение текста вопроса')
    def click_on_question(self, index):
        method, locator = MainPageLocators.faq_questions
        locator = locator.format(index)
        # Ждем загрузку вопроса
        self.wait_for_load_element((method, locator))
        # Кликаем вопрос
        question = self.find_element((method, locator))
        question.click()
        return question.text

    @allure.step('Получение ответа с номером {index}')
    def get_answer(self, index):
        method, locator = MainPageLocators.faq_answers
        locator = locator.format(index)
        # Ждем загрузку ответа
        self.wait_for_load_element((method, locator))
        return self.find_element((method, locator)).text
