from selenium import webdriver
import pytest
from selenium.webdriver.firefox import firefox_profile
from selenium.webdriver.firefox import firefox_binary


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome("C:\\seldriver\\chromedriver.exe")
        print("launching chrome")
    elif browser == 'edge':
        driver = webdriver.Edge("C:\\edgedriver\\msedgedriver.exe")
        print("launhing firefox")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
###################pytest html reports##############

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'saboor'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)