import os
import haksik_get

# HTML 저장 시작
menus_lunch = haksik_get.get_menu_310("lunch")
menus_dinner = haksik_get.get_menu_310("dinner")

# HTML 문자열 구성
html_content = "<html><head><meta charset='utf-8'><title>중앙대 오늘의 학식</title></head><body>"
html_content += "<h1>🍱 중앙대 학식 (310관 참슬기식당)</h1>"

html_content += "<h2>🍽️ 중식</h2><ul>"
for menus in menus_lunch:
    html_content += "<h4>" + menus[0] + "</h4><ul>"
    for menu in menus[1:]:
        html_content += "<li>" + menu + "</li>"
    html_content += "</ul>"
html_content += "</ul>"

html_content += "<h2>🌙 석식</h2><ul>"
for menus in menus_dinner:
    html_content += "<h4>" + menus[0] + "</h4><ul>"
    for menu in menus[1:]:
        html_content += "<li>" + menu + "</li>"
    html_content += "</ul>"
html_content += "</ul>"

html_content += "</body></html>"

# 폴더 만들기 + 파일 저장
os.makedirs("output", exist_ok=True)
with open("output/haksik_result.html", "w", encoding="utf-8") as f:
    f.write(html_content)
    print("HTML 저장 완료: output/haksik_result.html")