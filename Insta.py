# Instagram Album?

import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import os
import shutil
from selenium.webdriver.chrome.options import Options

images = re.compile(r'src="https://[-\w./"]*jpg')


def OpenBrowser():
    driver = webdriver.Firefox()
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--window-size=1920x1080")
    # chrome_driver = os.getcwd() + "\\chromedriver.exe"
    # driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
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
        last_height = new_height
        html_source = driver.page_source
        pics = re.findall(images, html_source)
        for item in pics:
            if item not in big_list:
                big_list.append(item)
        if new_height == last_height:
            break
    return big_list


def SaveImages(big_list):
    os.mkdir(account_name)
    urllib.request.urlretrieve(big_list[0][5:], account_name + '\\' + account_name + '.jpg')
    count = len(big_list) - 1
    for item in big_list:
        if count != len(big_list) - 1:
            urllib.request.urlretrieve(item[5:], account_name + '\\' + str(count + 1) + '.jpg')
        count -= 1


driver = OpenBrowser()
login(driver, '', '')
account_name = 'vishnugt95'
big_list = LoadAccount(account_name)
SaveImages(big_list)
