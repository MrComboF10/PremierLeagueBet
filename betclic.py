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
            EC.presence_of_element_located((By.CLASS_NAME, 'forms_inputText')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading page took too much time!")
    # elements = chrome_drive.find_elements_by_tag_name("input")
    username_input, password_input = chrome_drive.find_elements_by_class_name("forms_inputText")
    print(username_input.text)
    print(password_input.text)
    # username_input.send_keys(username)
    # password_input.send_keys(password)


def close():
    chrome_drive.close()


start()
register("MrComboF10", "abcd")
close()
