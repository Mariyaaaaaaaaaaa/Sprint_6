from selenium.webdriver.common.by import By


class BasePageLocators:

    scooter_button_header = [By.XPATH, ".//a[@href='/']"]
    logotype_yandex_button_header = [By.XPATH, ".//a[@href='//yandex.ru']"]
    cookie_button = [By.ID, "rcc-confirm-button"]

#  Главная страница
class MainPageLocators:

    header_title = [By.XPATH, "//div[contains(@class, 'Home_Header')]"]

    # Блок вопросов и ответов на main_page
    faq_list_of_questions = [By.CLASS_NAME, "accordion"]
    faq_questions = [By.XPATH, "(//div[@class='accordion__button'])[{}]"]
    faq_answers = [By.XPATH, "(//div[@class='accordion__panel'])[{}]"]

    # Кнопки заказа
    order_button_up = [By.CLASS_NAME, 'Button_Button__ra12g']  # [By.XPATH, "(.//button[text()='Заказать'])[1]"]
    order_button_down = [By.CLASS_NAME, 'Button_Middle__1CSJM']  # [By.XPATH, "(.//button[text()='Заказать'])[2]"]


# Страница заказа
class OrderPageLocators:

    # 1 страница:

    form_block = [By.XPATH, "//div[contains(@class, 'Order_Header')]"]
    next_button = [By.XPATH, ".//button[text()='Далее']"]
    input_fields = [By.XPATH, "(.//input)[{}]"]
    station_field = [By.XPATH, ".//div[@class='select-search']"]
    select_station_list = [By.XPATH, ".//div[@class='select-search__select']"]
    select_station_button = [By.XPATH, ".//ul/li/button[@value='{}']"]

    # Поле с выбранной станцией для проверки:                                    # Атрибут value
    station_value = [By.XPATH, ".//div[@class='select-search__value']/input"]

    # 2 страница:
    back_button = [By.XPATH, ".//button[text()='Назад']"]

    # Выбор даты доставки:                                                      # Атрибут value
    delivery_date = [By.XPATH, ".//div[@class='react-datepicker__input-container']/input"]

    # Элементы в календаре:
    week = [By.XPATH, ".//div[@class='react-datepicker__week']"]
    day = [By.CSS_SELECTOR, ".react-datepicker__day[tabindex='0']"]

    # Выбор срока аренды:
    rent_time_control = [By.XPATH, ".//div[@class='Dropdown-control']"]
    rent_time_menu = [By.XPATH, ".//div[@class='Dropdown-menu']"]
    rent_time_options = [By.XPATH, "(.//div[@class='Dropdown-option'])[{}]"]

    # Поле с выбранным сроком аренды:
    rent_time_is_selected = [By.XPATH, ".//div[@class='Dropdown-placeholder is-selected']"]

    # Цвет самоката:
    colour_black = [By.XPATH, "//input[@id='black']"]
    colour_grey = [By.XPATH, "//input[@id='grey']"]

    # Комментарий для курьера:
    commentary = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]

    # Кнопка Заказать на странице Заказа:
    order_button_order_page = [By.XPATH, "(.//button[text()='Заказать'])[2]"]   #//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]

    # Всплывающее окно подтверждения оформления заказа:
    confirm_order = By.XPATH, "//div[text()='Хотите оформить заказ?']"

    # Кнопка подтверждения заказа "Да"
    yes_button = [By.XPATH, ".//button[text()='Да']"]

    # Всплывающее окно "Заказ оформлен"
    order_is_completed = [By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"]   # "//div[@class='Order_ModalHeader__3FDaJ']"
