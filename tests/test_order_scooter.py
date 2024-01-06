import pytest
import allure

from pages.order_page import OrderPage
from data import OrderPageData
from locators import OrderPageLocators

from conftest import driver

class TestOrderPage:

    @allure.title('Проверка заполнения формы данных пользователя на странице оформления заказа')
    @allure.description('Заполнение формы "Для кого самокат" на странице оформления заказа и проверка введенных данных пользователя')
    @pytest.mark.parametrize('user, order', [[OrderPageData.user_1, OrderPageData.order_1], [OrderPageData.user_2, OrderPageData.order_2]])
    def test_order_page_form_1(self, driver, user, order):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        # Вводим данные пользователя в форму на странице заказа
        order_page.create_user(user)
        # Проверяем введенные данные пользователя
        assert order_page.check_input_value(2) == user['first_name']
        assert order_page.check_input_value(3) == user['last_name']
        assert order_page.check_input_value(4) == user['address']
        assert order_page.check_input_value(6) == user['telephone_number']


    @allure.title('Проверка заполнения данных формы об аренде на странице оформления заказа')
    @allure.description('Заполнение формы "Про аренду" на странице оформления заказа и проверка введенных данных заказа')
    @pytest.mark.parametrize('user, order', [[OrderPageData.user_1, OrderPageData.order_1], [OrderPageData.user_2, OrderPageData.order_2]])
    def test_order_page_form_2(self, driver, user, order):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        # Ввод данных пользователя в форму 1 на странице заказа
        order_page.create_user(user)
        # Клик по кнопке "Дальше"
        order_page.click_element(OrderPageLocators.next_button)
        # Ожидание перехода на 2ую страницу - загрузку кнопки "Назад"
        order_page.wait_for_load_element(OrderPageLocators.back_button)
        # Ввод данных заказа в форму 2 на странице заказа
        order_page.create_order(order)

        # Получаем введенные данные в полях и проверяем, что они соответствуют данным заказа
        assert order_page.check_value(OrderPageLocators.delivery_date) == order['delivery_date']
        assert order_page.check_text(OrderPageLocators.rent_time_is_selected) == order['rent_text']
        assert order_page.check_value(OrderPageLocators.commentary) == order['comment']


    @allure.title('Проверка позитивного сценария оформления заказа с двумя наборами данных')
    @allure.description('Заполнение формы заказа и проверка появления всплывающего окна с сообщением об успешном оформлении заказа')
    @pytest.mark.parametrize('user, order', [[OrderPageData.user_1, OrderPageData.order_1], [OrderPageData.user_2, OrderPageData.order_2]])
    def test_order_page_make_order(self, driver, user, order):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.create_user(user)
        order_page.click_element(OrderPageLocators.next_button)
        order_page.wait_for_load_element(OrderPageLocators.back_button)
        order_page.create_order(order)

        # Клик на кнопку "Заказать" внизу страницы
        order_page.click_element(OrderPageLocators.order_button_order_page)
        # Ожидание появления окна "Хотите оформить заказ?"
        order_page.wait_for_load_element(OrderPageLocators.confirm_order)
        # Клик на кнопку 'Да"
        order_page.click_element(OrderPageLocators.yes_button)
        # Ожидание всплывающего окна об успешном оформлении заказа
        order_page.wait_for_load_element(OrderPageLocators.order_is_completed)
        # Проверяем заголовок всплывающего окна "Заказ оформлен"
        assert OrderPageData.order_confirm_text in order_page.check_text(OrderPageLocators.order_is_completed)
