from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
import pytest
import time

@pytest.mark.add_promo_offer
class TestPromoOffersAdding():
  @pytest.mark.need_review
  @pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", pytest.param("7",  marks=pytest.mark.xfail), "8", "9"])
  def test_guest_can_add_product_to_basket(self, browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_in_product_page()

  @pytest.mark.xfail
  def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add()
    page.should_not_be_msg()

  def test_guest_cant_see_success_message(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_msg()

  @pytest.mark.xfail
  def test_message_disappeared_after_adding_product_to_basket(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add()
    page.should_not_be_mesag()

@pytest.mark.login_from_product
class TestGuestCanGoLoginPageFromProductPage():
  def test_guest_should_see_login_link_on_product_page(self, browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
  
  @pytest.mark.need_review
  def test_guest_can_go_to_login_page_from_product_page(self, browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()   

@pytest.mark.basket_from_product
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page_in_top()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_in_empty_basket_page()
             
@pytest.mark.basket_from_product_user
class TestUserAddToBasketFromProductPage():
  @pytest.fixture(scope='function', autouse = True)
  def setup(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    email = str(time.time()) + "@fakemail.org"
    password = str(time.time()) + "aezakmi"
    page.register_new_user(email, password)
    page.should_be_authorized_user()

  @pytest.mark.xfail
  def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add()
    page.should_not_be_msg()

  @pytest.mark.need_review
  def test_user_can_add_product_to_basket(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_in_product_page_user()


  
