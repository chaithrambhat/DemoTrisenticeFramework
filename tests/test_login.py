import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.alert import Alert


def test_login1(setup_and_teardown):
    lp = LoginPage(setup_and_teardown)
    lp.click_login_link()
    lp.enter_email("abc@gmail.com")
    lp.enter_password("abc!1234")
    lp.click_login_button()




#
# def test_login2(setup_and_teardown):
#     lp = LoginPage(setup_and_teardown)
#     lp.click_login_link()
#     lp.enter_email("dfghjkl@gmail.com")
#     lp.enter_password("asdfgh")
#     lp.click_login_button()
