import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception("Invalid browser option")

    driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
