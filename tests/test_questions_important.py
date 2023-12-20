from pages.home_page import HomePageScooter
from pages.base_page import BasePage
from data import ConstantData

class TestQuestion:
    def test_questions(self, driver):
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_home_page()
        home_page.scroll_questions()
        home_page.click_first_question()
        nav = home_page.get_description()

        assert nav.is_displayed()