from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time, json

def crawl_all_meals():
    options = Options()
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless=new") 
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--single-process")
    options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(options=options)
    result = {}

    try:
        driver.get("https://mportal.cau.ac.kr/main.do")
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        meals = [["morning", 10], ["lunch", 50], ["dinner", 80]]

        for meal, offset in meals:
            temp_dict = {}

            # 클릭 (조식, 중식, 석식)
            target_element = driver.find_element(By.XPATH, "//*[contains(text(), '조식')]")
            ActionChains(driver).move_to_element_with_offset(target_element, offset, 0).click().perform()
            time.sleep(0.2)

            # BeautifulSoup에 바로 넘기기
            soup = BeautifulSoup(driver.page_source, "html.parser")

            # 원하는 div 찾기
            divs = soup.find_all("div", class_="nb-p-04-detail")

            for ind, div in enumerate(divs):
                one_menu = {}
                try:
                    rest_name = div.find("p", class_="nb-p-04-02-01-a").text.strip()
                    price = div.find("p", class_="nb-p-04-02-02-b").text.strip()
                    foods = div.find("div", class_="nb-p-04-03 nb-font-13 nb-p-flex nb-wrap ng-binding")
                    foods = [p.text.strip() for p in foods.find_all("p")] if div else []

                    if price != "0 원" and len(foods) > 0:
                        one_menu["where"] = rest_name
                        one_menu["price"] = price
                        one_menu["menu"] = foods
                        temp_dict[ind] = one_menu

                except Exception as e:
                    print(f"Error while parsing html : \n {e}")

            result[meal] = temp_dict

    finally:
        driver.quit()
        
        with open("all_daily_menus.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)