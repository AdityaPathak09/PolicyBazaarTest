import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
        print("Launching chrome browser.........")
    elif browser == 'edge':
        driver = webdriver.Edge()
        driver.maximize_window()
        print("Launching edge browser.........")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# pytest HTML Report
def pytest_configure(config):
    config.option.metadata = {
        'Project Name': 'policyBazaar',
        'Module Name': 'Tester',
        'Tester': 'Team 5'
    }

# It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
