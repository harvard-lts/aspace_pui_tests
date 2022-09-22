import pytest
import selenium
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome('./chromedriver')

def test_first():
	driver.maximize_window()
	driver.get("https://www.python.org")
	title = driver.title
	assert title == 'Welcome to Python.org'
	driver.__exit__()

