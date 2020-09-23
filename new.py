
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
import pprint
pp = pprint.PrettyPrinter(indent=4)

def find_text(pattern, txt):
    re1 = re.compile(pattern)
    output = re1.findall(txt)
    if len(output) > 0:
        return output[0]
    else:
        return ''

def get_categories(dataset):
    output = []
    for ds in dataset:
        output.append(ds[1])
    return ','.join(output)


def find_text_multiple(pattern, txt):
    re1 = re.compile(pattern)
    output = re1.findall(txt)
    if len(output) > 0:
        return output
    else:
        return ''

def wongnai_merchant(driver, classname, list_url, place_name):
    output = []
    blocks = driver.find_elements_by_class_name(classname)

    for block in blocks:
        h = {}
        # title = block.find_element_by_xpath("//h2[@class='sc-1qge0b2-0 epxHvt sc-10ino0a-1 dkzaRG']").text
        
        h['place_name'] = place_name

        title_pattern = '<h(.+?) class="(sc-1qge0b2-0 epxHvt sc-10ino0a-1 dkzaRG|sc-1qge0b2-1 dPykew sc-10ino0a-1 dkzaRG)">(.+?)</h(.+?)>'
        result = find_text(title_pattern, block.get_attribute('innerHTML'))

        h['is_ads'] = True if result[0] == '5' else False
        h['title'] = result[2]

        floor_pattern = '<span class="sc-19l5fpm-0 fnWZPR"> (.+?)</span>'
        result = find_text(floor_pattern, block.get_attribute('innerHTML'))

        h['floor'] = result

        categories_pattern = '<a class="bbsi3i-1 gbjkpn" href="(.+?)">(.+?)</a>'
        result = find_text_multiple(categories_pattern, block.get_attribute('innerHTML'))
        h['categories'] = get_categories(result)

        rating_pattern = '<abbr title="(.+?)" class="sc-1iz478n-2 kypXeq">(.+?)</abbr>'
        result = find_text(rating_pattern, block.get_attribute('innerHTML'))
        h['rating'] = result
        if result != '':
            h['rating'] = result[1].replace('<!-- -->', '').strip()

        review_pattern = '<span class="sc-1uyabda-0 hcYpBY">(.+?) รีวิว</span>'
        result = find_text(review_pattern, block.get_attribute('innerHTML'))
        h['review'] = result

        review_pattern = '<span class="sc-1x0crv7-1 DjUfP">(.+?)</span>'
        result = find_text(review_pattern, block.get_attribute('innerHTML'))
        h['price'] = result

        review_pattern = '<span class="l5nsn2-0 bAFYpu">(.+?)</span>'
        result = find_text(review_pattern, block.get_attribute('innerHTML'))

        review_pattern = '<a class="du5f0f-0 kqmini" href="(.+?)"><span class="l5nsn2-0 bAFYpu">(.+?)</span> <!-- -->(.+?)</a>'
        result = find_text(review_pattern, block.get_attribute('innerHTML'))

        h['ranking'] = "{} {}".format(result[1], result[2]) if result != '' else result

        menu_recomment_pattern = '<div class="sc-10ino0a-9 gBYsUC">(.+?)</div>'
        result = find_text(menu_recomment_pattern, block.get_attribute('innerHTML'))
        h['menu_recomment'] = result

        h['list_url'] = list_url

        title_link_pattern = '<a class="sc-10ino0a-11 bDinEL" href="(.+?)">'
        result = find_text(title_link_pattern, block.get_attribute('innerHTML'))
        h['title_url'] = 'https://www.wongnai.com{}'.format(result)

        output.append(h)

    return output

def click_element_by_class(driver, classname, click_order):
    element = driver.find_elements_by_class_name(classname)
    element[click_order].click()

def get_next_prev_button_info(driver, classname):
    output = []
    blocks = driver.find_elements_by_class_name(classname)
    for block in blocks:
        output.append(block.text.split('\n'))
    return output

def run(first_url, place_name):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(first_url)


    class_of_close_notice_button = 'sc-AxiKw.cRbPuG'
    class_of_close_notice_button = 'sc-AxiKw.eAAKkt'

    sleep(1)

    click_element_by_class(driver, class_of_close_notice_button, 0)

    result = driver.page_source
    elements = []

    while True:
        list_url = driver.current_url
        print('Processing...')
        print(list_url)
        class_of_content = 'sc-1p1cxjo-0.idaVvx'
        wongnai_result = wongnai_merchant(driver, class_of_content, list_url, place_name)
        # print(wongnai_result)
        elements.append(wongnai_result)
        if len(wongnai_result) == 0:
            break
        else:
            btn_result = []
            class_of_next_page_button = 'sc-AxiKw.ghKQyp'
            class_of_next_page_button = 'sc-AxiKw.iTtrrq'
            btn_result = get_next_prev_button_info(driver, class_of_next_page_button)
            if len(btn_result) == 1 and 'ย้อนกลับ' in btn_result[0][0]:
                break
            click_element_by_class(driver, class_of_next_page_button, len(btn_result) - 1)
            sleep(10)

    print("Done")

    import csv


    csv_columns = elements[0][0].keys()
    csv_columns = list(csv_columns)

    csv_file = "{}_wongnai.csv".format(place_name)
    try:
        with open(csv_file, 'w', encoding="utf-8", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for element in elements:
                for data in element:
                    writer.writerow(data)
                    
    except IOError:
        print("I/O error")

# driver.get("https://www.wongnai.com/places/all-seasons-place?page.number=5")


run("https://www.wongnai.com/places/all-seasons-place", "All seasons place")
sleep(12)
run("https://www.wongnai.com/places/silom-complex", "Silom complex")
sleep(8)
run("https://www.wongnai.com/places/central-world", "Central world")
sleep(10)
run("https://www.wongnai.com/places/central-department-store-chit-lom", "Central department store chitlom")
sleep(15)
run("https://www.wongnai.com/places/empire-tower", "Empire tower")
