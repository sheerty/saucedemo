from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    checkout = '//button[@class="btn btn_action btn_medium checkout_button "]'

    #Getters

    def get_checkout(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout)))




    # Actions

    def click_checkout(self):
        self.get_checkout().click()
        print('check out successfully')




    # Methods

    def checkout_confirmed(self):
        self.get_current_url()
        self.click_checkout()



