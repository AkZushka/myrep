from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time

class ProductPage(BasePage): 
    def should_be_in_product_page(self):
        self.should_be_basket_button()
        self.go_to_basket_page()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button is not presented"

    def go_to_basket_page(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        self.should_be_in_basket_page()

    def should_be_in_basket_page(self):
        self.should_be_massage_add()
        self.should_be_correct_product_name()
        self.should_be_basket_price()
        self.should_be_correct_basket_price_simular_to_product_price()


    def should_be_massage_add(self):
        assert self.is_element_present(*ProductPageLocators.MASSAGE), "Massage of add is not presented"

    def should_be_correct_product_name(self):
        x1 = self.browser.find_element(*ProductPageLocators.MASSAGE_NAME).text
        x2 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert x1 == x2, "Product name is not correct"

    def should_be_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE1), "Basket price in top is not presented"
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE2), "Basket price in massage is not presented"

    def should_be_correct_basket_price_simular_to_product_price(self):
        tex = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert self.browser.find_element(*ProductPageLocators.BASKET_PRICE1).text.__contains__(tex), "Basket price in top is not correct"
        assert self.browser.find_element(*ProductPageLocators.BASKET_PRICE2).text == tex, "Basket price in massage is not correct"