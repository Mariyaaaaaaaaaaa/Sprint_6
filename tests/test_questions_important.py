import pytest
import allure

from pages.home_page import MainPage
from data import MainPageData
from locators import MainPageLocators

from conftest import driver

class TestMainPageQuestions:

    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном" на Главной странице')
    @allure.description('На Главной странице ищем вопрос, кликаем на него, проверяем, что открывается соответствующий текст')
    @pytest.mark.parametrize('index, question, answer', MainPageData.LIST_OF_QUESTIONS_AND_ANSWERS)
    def test_faq_questions_and_answers(self, driver, index, question, answer):
        main_page = MainPage(driver)
        # Открываем Главную страницу
        main_page.open_main_page()
        # прокручиваем страницу до списка вопросов
        main_page.scroll_to_element(MainPageLocators.faq_list_of_questions)
        # ждем появления списка вопросов
        main_page.wait_for_load_all_elements(MainPageLocators.faq_list_of_questions)
        # кликаем вопрос с номером 'index'
        question_received = main_page.click_on_question(index)
        # получаем соответствующий ответ
        answer_received = main_page.get_answer(index)
        # проверяем, что текст вопроса соответствует ожидаемому
        assert question_received == question
        # проверяем, что текст вопроса соответствует ожидаемому
        assert answer_received == answer