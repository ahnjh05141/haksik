from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

# CHROME_PATH = "/nix/store/zi4f80l169xlmivz8vja8wlphq74qqk0-chromium-125.0.6422.141/bin/chromium"
# CHROMEDRIVER_PATH = "/nix/store/3qnxr5x6gw3k9a9i7d0akz0m6bksbwff-chromedriver-125.0.6422.141/bin/chromedriver"

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)


def get_lunch():
    try:
        menus = []

        driver.get("https://mportal.cau.ac.kr/main.do")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        lunch_element = driver.find_element(By.XPATH, "//*[contains(text(), '조식')]")

        ActionChains(driver).move_to_element_with_offset(lunch_element, 50, 0).click().perform()
        time.sleep(0.1)

        html_text = driver.page_source

        menu1 = html_text.split("참슬기식당(310관 B4층)")[2]
        menu1 = menu1.split("\n")[7]
        menu1 = menu1.split("<p>")[1:]

        menu2 = html_text.split("참슬기식당(310관 B4층)")[3][:1000]
        menu2 = menu2.split("\n")[7]
        menu2 = menu2.split("<p>")[1:]

        temp = []
        for l in menu1:
            l = l.split("</p>")[0]
            temp.append(l)
        menus.append(temp)

        temp = []
        for l in menu2:
            l = l.split("</p>")[0]
            temp.append(l)
        menus.append(temp)
        return menus
    
    finally:
        driver.quit()


def get_dinner():
    try:
        menus = []

        driver.get("https://mportal.cau.ac.kr/main.do")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        lunch_element = driver.find_element(By.XPATH, "//*[contains(text(), '조식')]")

        ActionChains(driver).move_to_element_with_offset(lunch_element, 80, 0).click().perform()
        time.sleep(0.1)

        html_text = driver.page_source

        menu1 = html_text.split("참슬기식당(310관 B4층)")[2]
        menu1 = menu1.split("\n")[7]
        menu1 = menu1.split("<p>")[1:]

        menu2 = html_text.split("참슬기식당(310관 B4층)")[3][:1000]
        menu2 = menu2.split("\n")[7]
        menu2 = menu2.split("<p>")[1:]

        temp = []
        for l in menu1:
            l = l.split("</p>")[0]
            temp.append(l)
        menus.append(temp)

        temp = []
        for l in menu2:
            l = l.split("</p>")[0]
            temp.append(l)
        menus.append(temp)
        return menus
    
    finally:
        driver.quit()
