from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
chrome_driver_path_service = Service("C:/Development/chromedriver.exe")

driver = webdriver.Chrome(service=chrome_driver_path_service)
driver.refresh()
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
#
# print(article_count.text)
# # article_count.click()
#
# # all_portal = driver.find_element(by=By.LINK_TEXT, value="All portals")
# # all_portal.click()
#
# # Typing in
# search = driver.find_element(by=By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(by=By.NAME, value="fName")
print(fname)
fname.send_keys("Bhavya")

lname = driver.find_element(by=By.NAME, value="lName")
lname.send_keys("Rai")

email = driver.find_element(By.NAME, "email")
email.send_keys("example@gmail.com")

sign_up = driver.find_element(By.CLASS_NAME, "btn")
sign_up.click()


driver.quit()