from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Client_information_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    first_name = '//input[@data-test="firstName"]'
    last_name = '//input[@data-test="lastName"]'
    zip_code = '//input[@data-test="postalCode"]'
    continue_button ='//input[@data-test="continue"]'

    #Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_button)))




    # Actions

    def first_name_input(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('first_name input successfully')

    def last_name_input(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('lastname input successfully')

    def zip_code_input(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print('zip_code input successfully')

    def click_continue(self):
        self.get_continue_button().click()
        print('continue successfully')




    # Methods

    def client_information_input(self):
        self.get_current_url()
        self.first_name_input('Alex')
        self.last_name_input('Wanhatalo')
        self.zip_code_input('1295234')
        self.click_continue()


