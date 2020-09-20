from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("http://www.espn.com/nba/playbyplay?gameId=400974939")
driver.get("https://www.wongnai.com/places/all-seasons-place")

# https://www.wongnai.com/places/all-seasons-place

# load complete HTML file


element = driver.find_element_by_class_name("sc-AxiKw.cRbPuG")
element.click()

result = driver.page_source
# regular expression

blocks = driver.find_elements_by_class_name("sc-1p1cxjo-0.idaVvx")
for block in blocks:
	print(block.text.split('\n'))

element = driver.find_element_by_class_name("sc-AxiKw.ghKQyp")
element.click()
print('find solution to wait the page load complete before running next element')
# https://stackoverflow.com/questions/37787453/selenium-python-how-to-wait-for-a-page-to-load-after-a-click
print('==============')
sleep(10)
# element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "normal-priority-modal")))
blocks = driver.find_elements_by_class_name("sc-1p1cxjo-0.idaVvx")
for block in blocks:
	print(block.text.split('\n'))

# title = '<h2 class="sc-1qge0b2-0 epxHvt sc-10ino0a-1 dkzaRG">(.+?)</h2>'
# re1 = re.compile(title)
# title = re1.findall(result)
# print(len(title))

# rating = '<abbr title="(.+?)" class="sc-1iz478n-2 kypXeq">(.+?)</abbr>'
# re2 = re.compile(rating)
# rating = re2.findall(result)
# print(len(rating))

# review = '<span class="sc-1uyabda-0 hcYpBY">(.+?) รีวิว</span>'
# re3 = re.compile(review)
# review = re3.findall(result)
# print(len(review))

# price = '<span class="sc-1x0crv7-1 DjUfP">(.+?)</span>'
# re4 = re.compile(price)
# price = re4.findall(result)
# print(len(price))


# ranking = '<span class="l5nsn2-0 bAFYpu">(.+?)</span>'
# re5 = re.compile(ranking)
# ranking = re5.findall(result)
# print(len(ranking))

# menu_recomment = '<div class="sc-10ino0a-9 gBYsUC">(.+?)</div>'
# re6 = re.compile(menu_recomment)
# menu_recomment = re6.findall(result)
# print(len(menu_recomment))

# picture = '<div class="q07imc-1 eRwhKX">(.+?)</div>'
# re7 = re.compile(picture)
# picture = re7.findall(result)
# print(len(picture))

# element = driver.find_element_by_id("content")
# element = driver.find_element_by_tag_name("div")
# element = driver.find_element_by_name("contentBox")


