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
from selenium.webdriver.support.ui import Select

def find_text(pattern, txt):
    re1 = re.compile(pattern)
    output = re1.findall(txt)
    if len(output) > 0:
        return output[0]
    else:
        return ''

def get_element_content_by_class(driver, classname):
    output = []
    blocks = driver.find_elements_by_class_name(classname)
    for block in blocks:
        # import pdb; pdb.set_trace()
        output.append(block.text.split('\n'))
    return output

def click_element_by_class(driver, classname, click_order):
    element = driver.find_elements_by_class_name(classname)
    element[click_order].click()


driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.wongnai.com/places/all-seasons-place")
driver.get("https://www.hipflat.co.th/projects/rhythm-sukhumvit-42-lnymzl")
sleep(5)
driver.find_element_by_xpath('//a[@data-beds="2"]').click()
sleep(5)
page = 1
elements = driver.find_elements_by_xpath("//tr[@class='listing-row']")
for element in elements:
    numbers = element.find_elements_by_xpath('.//span[@class="number"]')
    idx = 0
    print(len(numbers))
    for n in numbers:
        parent = n.find_element_by_xpath('..')
        number = find_text('<span class="number">(.+?)</span>', parent.get_attribute('innerHTML'))
        unit = find_text('<span class="unit">(.+?)</span>', parent.get_attribute('innerHTML'))
        print(number)
        print(unit)
        # print('idx: ', idx)
        # if idx == 4:
            # print(n.get_attribute('innerHTML'))
        idx += 1
        # print(len(numbers))
        # print(numbers)

    # main = element.find_elements_by_xpath('.//div[@class="listing-row__primary"]')
    # main = element.find_element_by_xpath('.//div[@class="listing-row__primary"]')
    # second = element.find_element_by_xpath('.//div[@class="listing-row__secondary"]')
    # second = element.find_elements_by_xpath('.//div[@class="listing-row__secondary"]')
    # price_patterh = '<span class="money" data-money="(.+?)">'
    # total_price = find_text(price_patterh, main.get_attribute('innerHTML'))
    # unit_price = find_text(price_patterh, second.get_attribute('innerHTML'))

    # print(total_price, unit_price)
sleep(5)
page += 1
# driver.find_element_by_xpath('//a[@data-page="{}"]'.format(page)).click()
# sleep(5)
# elements = driver.find_elements_by_xpath("//tr[@class='listing-row']")
# for element in elements:
#     total_price = '<span class="money" data-money="(.+?)">'
#     result = find_text(total_price, element.get_attribute('innerHTML'))
#     print(result)


