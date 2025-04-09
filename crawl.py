from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time, html


def get_morning():
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
        driver.get("https://mportal.cau.ac.kr/main.do")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        target_element = driver.find_element(By.XPATH, "//*[contains(text(), '조식')]")

        ActionChains(driver).move_to_element_with_offset(target_element, 10, 0).click().perform()
        time.sleep(0.1)

        menus = {}

        html_text = driver.page_source

        temp_str = html_text.split("생활관식당(블루미르308관)")[2]
        temp_str = temp_str.split("\n")[7]
        temp_str = temp_str.split("<p>")[1:]

        menu_list = []
        for l in temp_str:
            l = l.split("</p>")[0]
            menu_list.append(l)
        menus['308'] = menu_list
    
    finally:
        driver.quit()


def get_lunch():
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
        driver.get("https://mportal.cau.ac.kr/main.do")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        target_element = driver.find_element(By.XPATH, "//*[contains(text(), '조식')]")
        ActionChains(driver).move_to_element_with_offset(target_element, 50, 0).click().perform()
        time.sleep(0.1)

        html_text = html.unescape(driver.page_source)

        menus = {}
        restaurants = [
                ['310-1', '참슬기식당(310관 B4층)', 2], 
                ['310-2', '참슬기식당(310관 B4층)', 3], 
                ['308', '생활관식당(블루미르308관)', 2], 
                ['309-1', '생활관식당(블루미르309관)', 2], 
                ['309-2', '생활관식당(블루미르309관)', 3], 
                ['309-3', '생활관식당(블루미르309관)', 4]
            ]
        for key, name, ind in restaurants:
            temp_str = html_text.split(name)[ind]
            temp_str = temp_str.split("\n")[7]
            temp_str = temp_str.split("<p>")[1:]

            menu_list = []
            for l in temp_str:
                l = l.split("</p>")[0]
                menu_list.append(l)
            menus[key] = menu_list

        return menus
    
    finally:
        driver.quit()


def get_dinner():
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
        driver.get("https://mportal.cau.ac.kr/main.do")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        target_element = driver.find_element(By.XPATH, "//*[contains(text(), '조식')]")
        ActionChains(driver).move_to_element_with_offset(target_element, 80, 0).click().perform()
        time.sleep(0.1)

        html_text = html.unescape(driver.page_source)

        menus = {}
        restaurants = [
                ['310-1', '참슬기식당(310관 B4층)', 2], 
                ['310-2', '참슬기식당(310관 B4층)', 3], 
                ['308', '생활관식당(블루미르308관)', 2], 
                ['309-1', '생활관식당(블루미르309관)', 2], 
                ['309-2', '생활관식당(블루미르309관)', 3], 
                ['309-3', '생활관식당(블루미르309관)', 4]
            ]
        for key, name, ind in restaurants:
            temp_str = html_text.split(name)[ind]
            temp_str = temp_str.split("\n")[7]
            temp_str = temp_str.split("<p>")[1:]

            menu_list = []
            for l in temp_str:
                l = l.split("</p>")[0]
                menu_list.append(l)
            menus[key] = menu_list

        return menus
    
    finally:
        driver.quit()