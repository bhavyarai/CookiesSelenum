# installing and setting selenium driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
chrome_driver_path_service = Service("C:/Development/chromedriver.exe")

# # executable path is deprecated
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=chrome_driver_path_service)
# Open a new browser window with the url
# driver.get("https://www.amazon.com")
driver.get("https://www.python.org")

# # Close : a particular tab
# driver.close()
name = driver.find_element(by=By.NAME, value="q")
print(name.get_attribute("placeholder"))


logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")
print(logo.text)
print(logo.parent)
titles = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]')

print(titles.text)

upcoming_events = titles.text.split("\n")
# close the browser: quit entire program
# dict = [ date : event for (date, event) in upcoming_events[2:]]
dict = {}
for i in range(2, len(upcoming_events)-1, 2):
    dict[i-2] = {"time": upcoming_events[i], "name": upcoming_events[i+1]}


print(upcoming_events)
print(dict)

print("\n using different method")
time = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
event = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")

for n in range(len(time)):
    print(time[n].text)
    print(event[n].text)

events = {i: {"time": time[i].text, "event": event[i].text} for i in range(len(time))}
print(events)
driver.quit()