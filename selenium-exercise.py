from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("http://sdetchallenge.fetch.com/")

i = 0
while i < 3:
    driver.find_element("id", "left_" + str(i)).send_keys(str(i))
    driver.find_element("id", "right_" + str(i)).send_keys(str(3 + i))
    i += 1

driver.find_element("id", "weigh").click()

time.sleep(3)

result_1 = driver.find_element(By.ID, "reset").text

j = 1
while j < 3:
    driver.find_element("id", "left_" + str(j)).send_keys(Keys.CONTROL + "a")
    driver.find_element("id", "left_" + str(j)).send_keys(Keys.DELETE)
    driver.find_element("id", "right_" + str(j)).send_keys(Keys.CONTROL + "a")
    driver.find_element("id", "right_" + str(j)).send_keys(Keys.DELETE)
    j += 1

right = 1 if result_1 == "<" else 4 if result_1 == ">" else 7
left = 0 if result_1 == "<" else 3 if result_1 == ">" else 6

driver.find_element("id", "left_0" ).send_keys(Keys.CONTROL + "a")
driver.find_element("id", "left_0").send_keys(str(left))
driver.find_element("id", "right_0").send_keys(Keys.CONTROL + "a")
driver.find_element("id", "right_0").send_keys(str(right))

driver.find_element("id", "weigh").click()

time.sleep(3)

result_2 = driver.find_element(By.ID, "reset").text

if result_1 == "<" and result_2 == "<":
    driver.find_element("id", "coin_0").click()
elif result_1 == "<" and result_2 == ">":
    driver.find_element("id", "coin_1").click()
elif result_1 == "<" and result_2 == "=":
    driver.find_element("id", "coin_2").click()
elif result_1 == ">" and result_2 == "<":
    driver.find_element("id", "coin_3").click()
elif result_1 == ">" and result_2 == ">":
    driver.find_element("id", "coin_4").click()
elif result_1 == ">" and result_2 == "=":
    driver.find_element("id", "coin_5").click()
elif result_1 == "=" and result_2 == "<":
    driver.find_element("id", "coin_6").click()
elif result_1 == "=" and result_2 == ">":
    driver.find_element("id", "coin_7").click()
else:
    driver.find_element("id", "coin_8").click()
