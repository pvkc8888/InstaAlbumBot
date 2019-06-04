# Instagram Album?

import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import os
import shutil
from selenium.webdriver.chrome.options import Options
import sys
import getpass

posts = re.compile(r'src="https://[/\S+/]*com')


def OpenBrowser():
    driver = webdriver.Firefox()
    return driver


def login(driver, username, password):
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(2)
    username_elem = driver.find_element_by_xpath('//*[@name="username"]')
    username_elem.clear()
    username_elem.send_keys(username)
    pass_element = driver.find_element_by_xpath('//*[@name="password"]')
    pass_element.send_keys(password)
    pass_element.send_keys(Keys.RETURN)
    time.sleep(2)


def GetAccount(account_name):
    driver.get('https://www.instagram.com/' + account_name)
    scroll_pause = 1
    last_height = driver.execute_script("return document.body.scrollHeight")
    big_list = []
    test = time.time()
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause)
        new_height = driver.execute_script("return document.body.scrollHeight")
        last_height = new_height
        html_source = driver.page_source
        pics = re.findall(posts, html_source)
        for item in pics:
            if item[5:] not in big_list:
                big_list.append(item[5:])
                print(big_list)
        # if new_height == last_height:
        #     break
        if time.time() - test > 120:
            break
    print(len(big_list))
    return big_list


def SaveImages(big_list):
    if not os.path.exists(account_name):
        os.mkdir(account_name)
    urllib.request.urlretrieve(big_list[0], account_name + '\\' + account_name + '.jpg')
    count = len(big_list) - 1
    for item in big_list:
        if count != len(big_list) - 1:
            urllib.request.urlretrieve(item, account_name + '\\' + str(count + 1) + '.jpg')
        count -= 1


if __name__ == "__main__":
    account_name = str(sys.argv[1])
    username = input('Enter username: ')
    password = getpass.getpass('Enter password: ')
    driver = OpenBrowser()
    login(driver, username, password)
    big_list = GetAccount(account_name)
    SaveImages(big_list)
