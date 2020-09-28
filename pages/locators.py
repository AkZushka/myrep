from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    MASSAGE = (By.CSS_SELECTOR, "#messages")
    MASSAGE_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_PRICE1 = (By.CSS_SELECTOR, ".basket-mini")
    BASKET_PRICE2 = (By.CSS_SELECTOR, ".alert-info strong")
    