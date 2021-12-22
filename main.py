import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('./chromedriver/chromedriver.exe')
browser.get("https://rozetka.ua")
browser.implicitly_wait(30)
search_term = "процесор"
browser.find_element_by_css_selector('[name="search"]').send_keys(search_term)
browser.find_element_by_css_selector('[name="search"]').send_keys(Keys.RETURN)
actual_text = browser.find_element_by_css_selector('h1.catalog-heading').text
except_text = search_term

assert actual_text.lower() == except_text

