import time

import pytest
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


@pytest.mark.run(order=1)
def test_buy_product_1(set_up):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )


        print('Start test 1')

        login = Login_page(driver)
        login.authorization()

        time.sleep(5)

        mp = Main_page(driver)
        mp.select_product_1()

        cp = Cart_page(driver)
        cp.checkout_confirmed()

        cip = Client_information_page(driver)
        cip.client_information_input()

        pp = Paypemnt_page(driver)
        pp.finish_payemnt()

        fp = Finish_page(driver)
        fp.finish()

        driver.quit()

@pytest.mark.run(order=2)
def test_buy_product_2(set_up):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )


        print('Start test 2')

        login = Login_page(driver)
        login.authorization()

        time.sleep(5)

        mp = Main_page(driver)
        mp.select_product_2()

        cp = Cart_page(driver)
        cp.checkout_confirmed()

        driver.quit()

@pytest.mark.run(order=3)
def test_buy_product_3(set_up):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )


        print('Start test 3')

        login = Login_page(driver)
        login.authorization()

        time.sleep(5)

        mp = Main_page(driver)
        mp.select_product_3()

        cp = Cart_page(driver)
        cp.checkout_confirmed()

        driver.quit()
