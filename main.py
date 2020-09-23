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
driver.get("https://www.wongnai.com/places/all-seasons-place?page.number=6")


class_of_close_notice_button = 'sc-AxiKw.cRbPuG'
click_element_by_class(driver, class_of_close_notice_button, 0)

result = driver.page_source


while True:
    class_of_content = 'sc-1p1cxjo-0.idaVvx'
    result = get_element_content_by_class(driver, class_of_content)
    print(result)
    if len(result) == 0:
        break
    else:
        btn_result = []
        class_of_next_page_button = 'sc-AxiKw.ghKQyp'
        btn_result = get_element_content_by_class(driver, class_of_next_page_button)
        if len(btn_result) == 1 and 'ย้อนกลับ' in btn_result[0][0]:
            break
        click_element_by_class(driver, class_of_next_page_button, len(btn_result) - 1)
        sleep(10)

print("Done")

# https://stackoverflow.com/questions/37787453/selenium-python-how-to-wait-for-a-page-to-load-after-a-click
# sleep(10)
# element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "normal-priority-modal")))
# blocks = driver.find_elements_by_class_name("sc-1p1cxjo-0.idaVvx")
# for block in blocks:
#     print(block.text.split('\n'))

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


