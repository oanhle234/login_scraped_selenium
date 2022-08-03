import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt

service = Service('chromedriver.exe')

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches',['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://automated.pythonanywhere.com/')
    return driver


def split_text(text):
    output = int(text.split(': ')[1])
    return output


def write_file(text):
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename, 'w') as file:
        file.write(text)


def main():
    driver = get_driver()
    time.sleep(1)
    driver.find_element(by='xpath', value='//*[@id="basicExampleNav"]/div/a').click()
    time.sleep(1)
    driver.find_element(by='id', value='id_username').send_keys('automated')
    driver.find_element(by='id', value='id_password').send_keys('automatedautomated' + Keys.RETURN)
    time.sleep(1)
    driver.find_element(by='xpath', value='/html/body/nav/div/a').click()
    while True:
        time.sleep(2)
        value = driver.find_element(by='xpath', value='/html/body/div[1]/div/h1[2]')
        text = str(split_text(value.text))
        write_file(text)
    
print(main())
