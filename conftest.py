from selenium import webdriver
import pytest

@pytest.fixture(autouse=True)
def setup_and_teardown():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.close()


# @pytest.fixture(params=['chrome','edge','firefox'])
# def setup_and_teardown(request):
#     parameter=request.param
#     if parameter=='chrome':
#         driver=webdriver.Chrome()
#     elif parameter=='edge':
#         driver=webdriver.Edge()
#     elif parameter=='firefox':
#         driver=webdriver.Firefox()
#
#     driver.get("https://demowebshop.tricentis.com/")
#     yield driver
#     driver.quit()
