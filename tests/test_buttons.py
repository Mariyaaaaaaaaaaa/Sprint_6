import pytest
import allure

from pages.home_page import MainPage
from pages.order_page import OrderPage
from data import ConstantData
from data import OrderPageData
from data import MainPageData
from locators import MainPageLocators
from locators import OrderPageLocators
from locators import BasePageLocators

from conftest import driver
class TestOrderButtons:

    @allure.title('Клик по кнопке "Заказать" на Главной странице')
    @allure.description('Проверяем, что по клику на кнопки "Заказать" - в хэдере и внизу Главной страницы - открывается страница заказа')
    @pytest.mark.parametrize('locator', [MainPageLocators.order_button_up, MainPageLocators.order_button_down])
    def test_order_buttons(self, driver, locator):
        main_page = MainPage(driver)
        # открываем Главную страницу
        main_page.open_main_page()
        # прокручиваем страницу до кнопки "Заказать"
        main_page.scroll_to_element(locator)
        # ждем загрузку кнопки Заказать
        main_page.wait_for_load_element(locator)
        # клик по кнопке Заказать
        main_page.click_element(locator)
        # ждем, что открылось страница оформления заказа с формой "Для кого самокат"
        main_page.wait_for_load_element(OrderPageLocators.form_block)
        # проверяем заголовок формы "Для кого самокат"
        assert OrderPageData.title_text in main_page.check_text(OrderPageLocators.form_block)
        # проверяем, что открылся URL страницы заказа
        assert driver.current_url == ConstantData.ORDER_URL

    @allure.title('Проверка открытия Главной страницы по клику на логотип Самокат на странице заказа')
    @allure.description('Проверяем, что по клику кнопки Самокат на странице заказа открывается Главная страница')
    def test_order_page_scooter_button(self, driver):
        order_page = OrderPage(driver)
        # открываем страницу заказа
        order_page.open_order_page()
        # клик по кнопке Самокат
        order_page.click_element(BasePageLocators.scooter_button_header)
        # ожидание открытия Главной страницы
        order_page.wait_for_load_element(MainPageLocators.faq_list_of_questions)
        # проверяем заголовка Главной страницы
        assert MainPageData.TITLE_TEXT in order_page.check_text(MainPageLocators.header_title)
        # проверяем, что открылся URL Главной страницы
        assert driver.current_url == ConstantData.BASE_URL


    @allure.title('Проверка клика по логотипу Яндекса на странице заказа')
    @allure.description('Проверяем, что по клику кнопки Яндекс на странице заказа в новом окне через редирект открывается главная страница Дзен')
    def test_order_page_logo_button(self, driver):
        order_page = OrderPage(driver)
        # открываем страницу заказа
        order_page.open_order_page()
        # кликаем на кнопку Яндекс
        order_page.click_element(BasePageLocators.logotype_yandex_button_header)
        # проверяем, что открылась новая вкладка
        assert order_page.check_new_window()
        # переключаемся на новую вкладку
        order_page.switch_to_new_window()
        #ждем загрузку в новой вкладке главной страницы Дзен через редирект
        order_page.wait_for_new_window(ConstantData.DZEN_URL)
        # проверяем, что открылась главная страница Дзен через редирект
        assert driver.current_url == ConstantData.DZEN_URL
