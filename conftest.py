
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CO
from selenium.webdriver.chrome.service import Service as CS
from selenium.webdriver.firefox.service import Service as FS
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["firefox"])  #, "chrome" - браузер Chrome не используем в задании, поэтому убран из параметризации
def driver(request):
    if request.param == "firefox":
        firefox_driver = GeckoDriverManager().install()
        service = FS(firefox_driver)
        driver = webdriver.Firefox(service=service)
    if request.param == "chrome":
        chrome_driver = ChromeDriverManager().install()
        service = CS(chrome_driver)
        options = CO()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
