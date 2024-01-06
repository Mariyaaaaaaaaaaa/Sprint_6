import allure

from pages.base_page import BasePage
from locators import OrderPageLocators
from data import ConstantData

class OrderPage(BasePage):
    """ Класс страницы заказа """

    @allure.step('Открываем страницу заказа по URL')
    def open_order_page(self):
        # открываем страницу заказа по URL
        self.open_page(ConstantData.ORDER_URL)

        # ждем загрузку страницы заказа
        self.wait_for_load_element(OrderPageLocators.next_button)

        # кликаем согласие с куки
        self.click_accept_cookies_button()

    @allure.step('Ждем загрузку страницы заказа')
    def wait_for_open_order_page(self):
        # ждем загрузку страницы заказа
        self.wait_for_load_element(OrderPageLocators.next_button)

    # Методы для работы с формой данных пользователя
    @allure.step('Ввод данных в форму "Для кого самокат" на странице заказа: {user}')
    def create_user(self, user):
        # заполняем текстовые поля ввода input, кроме станции метро (индексы 2, 3, 4, 6) информацией из набора данных пользователя
        self.set_input_value(2, user['first_name'])
        self.set_input_value(3, user['last_name'])
        self.set_input_value(4, user['address'])
        self.set_input_value(6, user['telephone_number'])

        # выбираем станцию метро из списка по индексу
        self.select_station(user['station_index'])

    @allure.step('Ввод текста в поле ввода input с номером {index}')
    def set_input_value(self, index, value):
        """ Вспомогательная функция: ввести текст в поле input по его индексу """
        method, locator = OrderPageLocators.input_fields
        locator = locator.format(index)
        self.find_element((method, locator)).send_keys(value)

    @allure.step('Получение значения поля ввода input с номером {index}')
    def check_input_value(self, index):
        """ Вспомогательная функция: получить значение поля input по его индексу """
        method, locator = OrderPageLocators.input_fields
        locator = locator.format(index)
        return self.find_element((method, locator)).get_attribute("value")

    @allure.step('Выбор станции из списка по индексу: {index}')
    def select_station(self, index):
        # кликаем поле выбора станции
        self.click_element(OrderPageLocators.station_field)

        # ждем появления выпадающего списка станций
        self.wait_for_presence_of_element(OrderPageLocators.select_station_list)

        # кликаем станцию в списке
        method, locator = OrderPageLocators.select_station_button
        locator = locator.format(index)
        self.click_element((method, locator))

    @allure.step('Получение названия выбранной станции')
    def check_station(self):
        return self.find_element(OrderPageLocators.station_value).get_attribute("value")

    # Методы для работы с формой данных о заказе
    @allure.step('Ввод данных в форму "Про аренду" на странице заказа {order}')
    def create_order(self, order):
        # Выбираем дату в поле 'Когда привезти самокат'
        self.select_delivery_date(order['delivery_date'])
        # выбираем срок аренды по индексу: 1-7 суток
        self.select_rent_time(order['rent_days'])
        # Выбираем цвет самоката (True/False)
        if order['black']:  # выбираем цвет 'Черный жемчуг'
            self.click_element(OrderPageLocators.colour_black)
        if order['grey']:  # выбираем цвет 'Серая безысходность'
            self.click_element(OrderPageLocators.colour_grey)
        # Вводим комментарий для курьера (поле ввода с индексом 4)
        if order['comment']:
            self.set_value(OrderPageLocators.commentary, order['comment'])

    @allure.step('Выбор даты доставки {delivery_date} в поле "Когда привезти самокат?"')
    def select_delivery_date(self, delivery_date):
        self.set_value(OrderPageLocators.delivery_date, delivery_date)

        # кликаем на поле даты, чтобы открылся календарь с введенной датой
        #   (или текущей датой, если дата не указана)
        self.click_element(OrderPageLocators.delivery_date)

        # ждем появления элементов календаря - неделя и день
        self.wait_for_presence_of_element(OrderPageLocators.week)
        self.wait_for_presence_of_element(OrderPageLocators.day)

        # ищем выбранный день в календаре и кликаем по нему
        self.click_element(OrderPageLocators.day)

    @allure.step('Выбор срока аренды (1-7 дней: {index})')
    def select_rent_time(self, index):
        # кликаем поле выбора срока аренды
        self.click_element(OrderPageLocators.rent_time_control)

        # ждем загрузку выпадающего списка сроков аренды - от 1 до 7 суток
        self.wait_for_presence_of_element(OrderPageLocators.rent_time_menu)

        # кликаем элемент списка с индексом {index}
        method, locator = OrderPageLocators.rent_time_options
        locator = locator.format(index)
        self.click_element((method, locator))
