from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    cart = '//a[@class="shopping_cart_link"]'
    select_product1 = '//button[@data-test="add-to-cart-sauce-labs-backpack"]'
    select_product2 = '//button[@data-test="add-to-cart-sauce-labs-bike-light"]'
    select_product3 = '//button[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]'
    burger = '//button[@id="react-burger-menu-btn"]'
    about = '//a[@id="about_sidebar_link"]'

    #Getters

    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product1)))

    def get_product_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product2)))

    def get_product_3(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_burger(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.burger)))

    def get_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about)))





    # Actions

    def click_select_product_1(self):
        self.get_product_1().click()
        print('click select product 1 successfully')
    def click_select_product_2(self):
        self.get_product_2().click()
        print('click select product 2 successfully')
    def click_select_product_3(self):
        self.get_product_3().click()
        print('click select product 3 successfully')
    def click_cart(self):
        self.get_cart().click()
        print('click cart successfully')
    def click_burger(self):
        self.get_burger().click()
        print('click burger successfully')
    def click_about(self):
        self.get_about().click()
        print('click about successfully')



    # Methods

    def select_product_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_product_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_product_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()

    def about_link(self):
        self.get_current_url()
        self.click_burger()
        self.click_about()
        self.assert_url('https://saucelabs.com/')



