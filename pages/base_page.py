from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import BasePageLocators
from data import ConstantData


""" Базовый класс для главной страницы и страницы заказа """
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    """  Общие методы  """

    """ Открытие страницы """
    def open_page(self, url):
        self.driver.get(url)

    """ Ожидание загрузки элемента """
    def wait_for_load_element(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))

    """ Ожидание открытия страницы при переходе по ссылке """
    def wait_for_open_page(self, page_url):

        return WebDriverWait(self.driver, 10).until(
                    expected_conditions.url_to_be(page_url))

    """ Ожидание появления элемента """
    def wait_for_presence_of_element(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(locator))

    """ Поиск элемента """
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    """ Поиск элементов """
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    """ Клик по элементу """
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    """ Ввод текста в поле """
    def set_value(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    """ Получение значения  """
    def check_value(self, locator):
        return self.driver.find_element(*locator).get_attribute("value")

    """ Получение текста """
    def check_text(self, locator):
        return self.driver.find_element(*locator).text


    """  Специальные методы для работы со страницами  """


    """  Скролл страницы до элемента """
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    """  Проверка открытия новой вкладки """
    def check_new_window(self):
        return len(self.driver.window_handles) > 1

    """ Переключение на новую вкладку """
    def switch_to_new_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    """ Ожидание загрузки в новой вкладке главной страницы Яндекс Дзен """
    def wait_for_new_window(self, new_url=data.DZEN_URL):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_changes(data.BLANK_URL))
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be(new_url))

    """  Согласие с куки """
    def click_accept_cookies_button(self):
        self.driver.find_element(*base_page_locators.cookie_button).click()