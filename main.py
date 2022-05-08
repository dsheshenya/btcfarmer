from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep

nickname = ''
password = ''


driver = webdriver.Firefox()

def login():
    driver.get("http://adbtc.io/login")

    login_box = driver.find_element_by_name('email_or_username')
    password_box = driver.find_element_by_name('password')

    login_box.send_keys(nickname)
    password_box.send_keys(password)

    while driver.title.startswith('login'):
        sleep(1)

def go_to_url():
    visit_time_element = driver.find_element_by_class_name('display-4')
    visit_time = int(''.join(list(filter(str.isdigit, visit_time_element.text))))

    sleep(1)

    button = driver.find_element_by_id('gotourl')
    button.send_keys(Keys.RETURN)
    driver.switch_to.window(driver.window_handles[1])

    sleep(visit_time + 1)

    driver.close()

    sleep(1)
    

login()

while True:
    go_to_url()

    sleep(2)
    driver.switch_to.window(driver.window_handles[0])
