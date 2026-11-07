password = input("비밀번호를 입력하세요:")

while password != "python123" :
    print("비밀번호가 틀렸습니다. 다시 입력하세요.")
    password = input("비밀번호를 입력하세요:")
else:
   print("로그인 성공! 환영합니다")
