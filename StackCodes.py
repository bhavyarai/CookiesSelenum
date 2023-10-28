from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
s = Service('C:/Development/chromedriver.exe')
browser = webdriver.Chrome(service=s)
url = 'https://www.google.com'
browser.get(url)
my_name = browser.find_element(by=By.NAME, value="q")
my_name.send_keys("Bhavya Rai")
my_name.send_keys(Keys.ENTER)

# browser.quit()