import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import ConstantData


class HomePageScooter:
    """ logotype_scooter = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    button_order_up = [By.CLASS_NAME, 'Button_Button__ra12g']
    button_order_down = [By.CLASS_NAME, '*Button_Middle__1CSJM'] #Button_Button__ra12g
    questions = [By.XPATH, './/div[text()="Вопросы о важном"]']
    scooter_img = [By.XPATH, './/img[@alt="Scooter blueprint"]']
    element_question = [By.XPATH, './/div[@class="Home_FourPart__1uthg"]']
    first_question = [By.ID, 'accordion__heading-0']  #Сколько это стоит? И как оплатить?']
    first_answer = [By.XPATH, './/p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]']  """


    def __init__(self, driver):
        self.driver = driver
        self.base_url = ConstantData.BASE_URL

        # метод кликает на кнопку добавления нового места

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(*self.scooter_img))

    def scroll_questions(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", *self.element_question)

    def click_first_question(self):
        self.driver.find_element(*self.first_question).click()


    def get_description(self):
        return self.driver.find_element(*self.first_answer).text

    #a = self.driver.find_element(*self.first_answer).text
    #print(a)



    """
    questions_important_list = 
    [
    'Сколько это стоит? И как оплатить?'
    'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    'Хочу сразу несколько самокатов! Так можно?'
    'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    'Как рассчитывается время аренды?'
    'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    'Можно ли заказать самокат прямо на сегодня?'
    'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    'Можно ли продлить заказ или вернуть самокат раньше?'
    'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    'Вы привозите зарядку вместе с самокатом?'
    'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    'Можно ли отменить заказ?'
    'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    'Я жизу за МКАДом, привезёте?'
    'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    ]
    """




