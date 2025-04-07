from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time


def get_menu_310():
    options = Options()
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless=new") 
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--single-process")
    options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(options=options)

    try:
        menus = []

        driver.get("https://mportal.cau.ac.kr/main.do")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

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

get_menu_310()