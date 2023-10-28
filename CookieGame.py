from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path_service = Service("C:/Development/chromedriver.exe")

driver = webdriver.Chrome(service=chrome_driver_path_service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.refresh()
# get cookie to click on
cookie = driver.find_element(By.ID, "cookie")

# get upgrade items ids
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

# set timing
timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    # every five second
    if time.time() > timeout:

        # get all upgrade <b> tags
        all_costs = driver.find_elements(By.CSS_SELECTOR, '#store b')
        items_prices = []

        # Convert <b> text onto an integer price.
        for price in all_costs:
            element_text = price.text
            # print(element_text)
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                items_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {items_prices[n]: item_ids[n] for n in range(len(all_costs)-1)}
        # print(cookie_upgrades)

        # get current cookie count
        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # find upgrades that we can afford
        affordable_upgrades = {cost: id for (cost, id) in cookie_upgrades.items() if cookie_count > cost}
        # print(affordable_upgrades)

        # Purchase the most expensive affordable upgrade
        if affordable_upgrades:
            highest_price_aff = max(affordable_upgrades)
            # print(highest_price_aff)

            to_purchase_id = affordable_upgrades[highest_price_aff]

            driver.find_element(by=By.ID, value=to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 10

        # After 5 minutes stop the bot and check the cookies per second count.
        if time.time() > five_min:
            cookie_per_s = driver.find_element(by=By.ID, value="cps").text
            print(cookie_per_s)
            break