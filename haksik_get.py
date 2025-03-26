from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

def get_menu_310(which_time):
    menus = []
    options = Options()
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    options.add_argument("--window-size=1280,1440")
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.get("https://mportal.cau.ac.kr/main.do")

    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)

    if which_time == "lunch":
        click_positions = [
            (380, 930),
            (380, 1050),
            (380, 1020)
        ]
    else:
        click_positions = [
            (420, 930),
            (380, 1050),
            (380, 1020)
        ]

    params = ["생활관식당(블루미르308관)", "5,500 원", "4,000 원"]

    pointer = PointerInput(kind="mouse", name="mouse")
    actions = ActionBuilder(driver, mouse=pointer)

    for idx, (x, y) in enumerate(click_positions):
        try:
            actions.pointer_action.move_to_location(x, y)
            actions.pointer_action.click()
            actions.perform()
            time.sleep(0.1)

            if idx > 0:
                body_text = driver.find_element("tag name", "body").text
                body_text = body_text.split('\n')
                tar1 = body_text.index(params[idx])
                tar2 = body_text.index(params[0])
                res = body_text[tar1: tar2+1-idx]

                menus.insert(0, res)

            time.sleep(0.1)

        except Exception as e:
            menus = f"에러 발생: {e}"

    driver.quit()

    for menu in menus:
        print(menu)

    return menus