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
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    TOP_TO_BASKET = (By.CSS_SELECTOR, ".btn-group .btn-default")

class BasketPageLocators():
    MESSAGE_EMPTY = (By.XPATH, "//body/div/div/div/div/p/a")
    ELEMENT_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-4")
    