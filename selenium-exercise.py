import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("http://sdetchallenge.fetch.com/")

for i in range(3):
    driver.find_element("id", "left_" + str(i)).send_keys(str(i))
    driver.find_element("id", "right_" + str(i)).send_keys(str(3 + i))

driver.find_element("id", "weigh").click()
time.sleep(3)
result = driver.find_element("id", "reset").text


for i in range(1,3):
    driver.find_element("id", "left_" + str(i)).send_keys(Keys.CONTROL + "a")
    driver.find_element("id", "left_" + str(i)).send_keys(Keys.DELETE)
    driver.find_element("id", "right_" + str(i)).send_keys(Keys.CONTROL + "a")
    driver.find_element("id", "right_" + str(i)).send_keys(Keys.DELETE)

answer = 0 if result == "<" else 3 if result == ">" else 6

driver.find_element("id", "left_0" ).send_keys(Keys.CONTROL + "a")
driver.find_element("id", "left_0").send_keys(str(answer))
driver.find_element("id", "right_0").send_keys(Keys.CONTROL + "a")
driver.find_element("id", "right_0").send_keys(str(answer + 1))

driver.find_element("id", "weigh").click()
time.sleep(3)
result = driver.find_element("id", "reset").text

answer += 0 if result == "<" else 1 if result == ">" else 2
driver.find_element("id", "coin_" + str(answer)).click()
