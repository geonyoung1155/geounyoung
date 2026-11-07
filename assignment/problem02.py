num1 = input("숫자 1을 입력하세요")
num2 = input("숫자 2를 입력하세요")
op = input("연산자를 입력하세요")

if num1.isdigit() and num2.isdigit():
        if op == "+":
          print(int(num1) + int(num2))
        elif op == "-":
          print(int(num1) - int(num2))
        elif op == "*":
          print(int(num1) * int(num2))
        elif op == "/":
          print(int(num1) / int(num2))
        else:
          print("잘못된 입력입니다.")

else:
  print("숫자가 아닌 입력을 했습니다.")
