arr = ["apple", "banana", "cherry"]

print("메뉴 리스트")
for item in arr:
    print(item)

print("-----------------------")
print("메뉴 리스트")
sale_list = {'apple':1, 'banana':0, 'cherry':3}
for key in sale_list:
    if sale_list[key] == 0:
            print(key, "sold out")
    else:
        print(key, sale_list[key])


print(range(10))

for i in range(10):
    print(i)
"""
# while 문으로 동일하게 수행하려면
a = 0
while a < 10:
    print(a)
    a += 1 
"""


print("-------------------")
ex_arr = [nun * 2 for nun in range(10)]
print(ex_arr)

# 학생들의 점수를 이용해서
#1. 개인별 평균점수를 구할것
#2. 이름으로 검색해서 성적을 따보기
#3. 과목별 최고 득점자

class_scores = {
    "김철수": {"국어": 85, "영어": 90, "수학": 78, "과학": 92},
    "이영희": {"국어": 92, "영어": 88, "수학": 95, "과학": 96},
    "박민수": {"국어": 76, "영어": 65, "수학": 82, "과학": 70},
    "정수진": {"국어": 88, "영어": 94, "수학": 90, "과학": 89},
    "한동석": {"국어": 60, "영어": 72, "수학": 65, "과학": 58}
}

# 학생별 평균 점수
for

# 과목별 최고 득점자