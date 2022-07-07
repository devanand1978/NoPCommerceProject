from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        s = Service(executable_path=r"C:\Users\DEV-A\Downloads\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        print("********* Launch Chrome Browser ****************")
    elif browser == 'firefox':
        s = Service(executable_path=r"C:\Users\DEV-A\Downloads\geckodriver-v0.31.0-win64\geckodriver.exe")
        driver = webdriver.Firefox(service=s)
        print("********* Launch Firefox Browser ****************")
    else:
        s = Service(executable_path=r"C:\Users\DEV-A\Downloads\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        print("********* Launch Chrome Browser ****************")
    return driver



def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

##### HTML REPORT #####

def pytest_configure(config):
    config._metadata['Project Name']='NoPCommerce'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='Devanand Kumar'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
