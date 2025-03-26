from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

def get_menu_310():
    menus = []
    options = Options()
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    options.add_argument("--window-size=1280,1440")
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.get("https://mportal.cau.ac.kr/main.do")

    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    lunch_element = driver.find_element(By.XPATH, "//*[contains(text(), '참슬기식당')]")
    location = lunch_element.location
    size = lunch_element.size

    ActionChains(driver).move_to_element_with_offset(lunch_element, 0, 60).click().perform()
    time.sleep(0.1)

    html_text = driver.page_source
    menu1 = html_text.split("참슬기식당(310관 B4층)")[2]
    menu1 = menu1.split("\n")[7]
    menu1 = menu1.split("<p>")[1:]

    menu2 = html_text.split("참슬기식당(310관 B4층)")[3][:1000]
    menu2 = menu2.split("\n")[7]
    menu2 = menu2.split("<p>")[1:]

    # print(lunch, dinner)

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

    time.sleep(3.0)
    driver.quit()

    return menus