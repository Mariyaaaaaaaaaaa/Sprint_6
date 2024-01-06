import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import BasePageLocators
from data import ConstantData


class BasePage:
    """ Базовый класс для Главной страницы и страницы заказа """

    @allure.step('Открываем браузер')
    def __init__(self, driver):
        self.driver = driver

    """  Общие методы  """

    def open_page(self, url):
        """ Открытие страницы """
        self.driver.get(url)

    def wait_for_load_element(self, locator):
        """ Ожидание загрузки элемента """
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_for_load_all_elements(self, locator):
        """ Ожидание загрузки всех элементов """
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_all_elements_located(locator))

    def wait_for_open_page(self, page_url):
        """ Ожидание открытия страницы при переходе по ссылке """
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be(page_url))

    def wait_for_presence_of_element(self, locator):
        """ Ожидание появления элемента """
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(locator))

    def find_element(self, locator):
        """ Поиск элемента по локатору """
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """ Поиск элементов по локатору """
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        """ Клик по элементу """
        self.driver.find_element(*locator).click()

    def set_value(self, locator, value):
        """ Ввод текста в поле """
        self.driver.find_element(*locator).send_keys(value)

    def check_value(self, locator):
        """ Получение значения  """
        return self.driver.find_element(*locator).get_attribute("value")

    def check_text(self, locator):
        """ Получение текста """
        return self.driver.find_element(*locator).text


    """  Специальные методы для работы со страницами  """

    @allure.step('Прокручиваем страницу до элемента по локатору')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Проверяем открытие новой вкладки')
    def check_new_window(self):
        return len(self.driver.window_handles) > 1

    @allure.step('Переключение на новую вкладку')
    def switch_to_new_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Ожидание загрузки в новой вкладке главной страницы Яндекс Дзен через редирект')
    def wait_for_new_window(self, new_url=ConstantData.DZEN_URL):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.url_changes(ConstantData.BLANK_URL))
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.url_to_be(new_url))

    @allure.step('Кликаем согласие с куки')
    def click_accept_cookies_button(self):
        self.driver.find_element(*BasePageLocators.cookie_button).click()
