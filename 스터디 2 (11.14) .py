#프로그래밍 스터디 과제 (11.14)
#05) 주사위 두개의 합이 n인 경우 구하기
n = int(input("12이하의 정수를 입력하시오. : "))
i = 1
while i <= 6:
    j = 1
    while j <= 6:
        if i + j == n :
            print("주사위 2개의 합이 %d인 경우는 (%d, %d)인 경우이다."%(n,i,j))
        j += 1
    i += 1
print()

#06) 주사위를 던진 후에 두개의 합이 6이 나오는 확률값을 이론과 비교하기
import random

times = 0
y = 1

while y <= 1000 :
    i = random.randint(1,6)
    j = random.randint(1,6)
    i + j
    if i + j == 6 :
        times += 1
    y += 1
if times == 139 :
    print("확률이 이론과 일치한다.")
else :
    print("확률이 이론과 불일치한다.")
print()
        
#07) 위의 중복 반복문에 지역 리스트를 추가해서 조합을 생성해보자.
persons = ["김 씨", "박 씨", "이 씨"]
restaurants = ["한식", "미국식", "프랑스식"]
locations = ["서울", "부산", "대전"]
for p in persons :
    for r in restaurants :
        for l in locations :
             print("%s가 %s에 위치한 %s 식당을 방문"%(p,l,r))
    print()
print()
