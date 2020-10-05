from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_in_empty_basket_page(self):
        self.should_be_empty_basket()
        self.should_be_message_empty_basket()

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ELEMENT_IN_BASKET), "Basket is not empty"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY), "Message of empty basket is not presented"
        
        
    
