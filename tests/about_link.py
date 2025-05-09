import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.paypemnt_page import Paypemnt_page


def test_link_about():
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )


        print('Start test')

        login = Login_page(driver)
        login.authorization()

        time.sleep(5)

        mp = Main_page(driver)
        mp.about_link()

        driver.quit()

