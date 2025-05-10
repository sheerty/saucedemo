import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Paypemnt_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    finish_button = '//button[@class="btn btn_action btn_medium cart_button"]'

    #Getters

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.finish_button)))




    # Actions

    def click_finish(self):
        self.get_finish_button().click()
        print('finish')




    # Methods

    def finish_payemnt(self):
        with allure.step('finish payemnt'):
            Logger.add_start_step(method='finish_payment')
            self.get_current_url()
            self.click_finish()
            Logger.add_end_step(url=self.driver.current_url, method='finish_payment')



