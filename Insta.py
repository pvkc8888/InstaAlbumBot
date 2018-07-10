# Instagram Album?

import time
import selenium
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request

images = re.compile(r'src="https://[-\w./"]*jpg')


def OpenBrowser():
    driver = webdriver.Firefox()
    return driver


def login(driver, username, password):
    driver.get('https://www.instagram.com')
    time.sleep(3)
    login_button = driver.find_element(By.XPATH, '//a[@href = "/accounts/login/"]')
    login_button.click()
    time.sleep(2)
    username_elem = driver.find_element_by_xpath('//*[@name="username"]')
    username_elem.clear()
    username_elem.send_keys(username)
    pass_element = driver.find_element_by_xpath('//*[@name="password"]')
    pass_element.send_keys(password)
    pass_element.send_keys(Keys.RETURN)
    time.sleep(2)


def LoadAccount(account_name):
    driver.get('https://www.instagram.com\\' + account_name)
    scroll_pause = 1
    last_height = driver.execute_script("return document.body.scrollHeight")
    big_list = []
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        html_source = driver.page_source
        pics = re.findall(images, html_source)
        for item in pics:
            if item not in big_list:
                big_list.append(item)
    return big_list


def SaveImages(big_list):
    count = 1
    for item in big_list:
        urllib.request.urlretrieve(item[5:], str(count) + '.jpg')
        count += 1


driver = OpenBrowser()
login(driver, 'your_username', 'your_password')
account_name = 'target_user_name_here'
big_list = LoadAccount(account_name)
SaveImages(big_list)
