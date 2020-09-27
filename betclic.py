from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def start():
    global chrome_drive, betclic_url, betclic_login_url, premier_league_url, delay
    chrome_drive = webdriver.Chrome("C:\\Users\\pcost\\chromedriver_win32\\chromedriver.exe")
    betclic_url = "https://www.betclic.pt/"
    betclic_login_url = "https://www.betclic.pt/login?returnUrl=%2F"
    premier_league_url = "https://www.betclic.pt/futebol-s1/inglaterra-premier-lg-c3"
    delay = 10


def register(username, password):
    chrome_drive.get(betclic_login_url)
    try:
        myElem = WebDriverWait(chrome_drive, delay).until(
            EC.presence_of_element_located((By.ID, 'loginPage_username')))
        myElem = WebDriverWait(chrome_drive, delay).until(
            EC.presence_of_element_located((By.ID, 'loginpage_password')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading page took too much time!")

    username_input = chrome_drive.find_element_by_id("loginPage_username").find_element_by_class_name("forms_inputText")
    password_input = chrome_drive.find_element_by_id("loginpage_password").find_element_by_class_name("forms_inputPassword")
    button = chrome_drive.find_element_by_tag_name("button")

    chrome_drive.implicitly_wait(10)

    username_input.send_keys(username)
    password_input.send_keys(password)
    button.click()


def close():
    chrome_drive.close()


start()
register("MrComboF10", "abcd")
# close()
