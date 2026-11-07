age = int(input("나이를 입력하세요:"))

if age < 8:
    print("무료입니다.")
elif age < 20:
    print("10,000원입니다.")
elif age < 65:
    print("20,000원입니다.")
elif age > 64:
    print("5000원입니다.")