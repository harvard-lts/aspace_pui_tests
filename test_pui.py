import pytest
import selenium
import os
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

_base_url = os.getenv('BASE_URL')

def test_first(driver):
	driver.maximize_window()
	driver.get(str(_base_url))
	title = driver.title
	print(title)
	assert title == 'Hollis Archival Collection Guides | HOLLIS for'

@pytest.fixture(scope='session', autouse=True)
def driver():
	# Will be executed before the first test
	options = Options()
	options.add_argument('--headless')
	options.add_argument('--disable-gpu')
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
	yield driver
	# Will be executed after the last test
	driver.quit()

