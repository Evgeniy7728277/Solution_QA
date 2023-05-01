"""This module contains shared fixtures"""
import json
from selenium.webdriver.chrome.service import Service
import pytest
import selenium.webdriver


@pytest.fixture
def config(scope='session'):
    #Read the json file
    with open('config.json') as config_file:
        config = json.load(config_file)
    #Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    #Return the config so it can be used
    return config


@pytest.fixture
def browser(config):
    if config['browser'] == 'Chrome':
        browser = selenium.webdriver.Chrome()
    elif config['browser'] == 'FireFox':
        browser = selenium.webdriver.Firefox()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        browser = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    #Maki its calls wait for elements to appear
    browser.implicitly_wait(config['implicit_wait'])

    #Return the wbDriver instance for setup
    yield browser

    browser.quit()

    service = Service('C:\\Users\\EvgeniyBelsky\\Desktop\\ManagerLayer\\chromedriver_win32\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    driver.get('http://192.168.110.13:8091/Qa/ManagementLayer/index.html#/installations/QPC/Applications')
    driver.implicitly_wait(5)
    yield driver
    driver.quit()