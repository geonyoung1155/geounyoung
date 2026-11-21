menu = {
    "삼각김밥": 1200,
    "바나나우유": 1700,
    "컵라면": 1500,
    "샌드위치": 2500
}

# print(menu["삼각김밥"]) # value에 직접 접근하는 방법
# print(menu.keys())
# print(menu.values())
# print(menu.items()) #(key, value)

print("====================")
for item in menu:
    print(item, ":", menu[item])
print("====================")

user_menu = input("메뉴를 입력하세요 > ")

has_menu = False
for item in menu:
    if item == user_menu:
        print("가격은", menu[item], "원입니다.")
        has_menu = True

if has_menu == False:
    print("없는 메뉴입니다.")