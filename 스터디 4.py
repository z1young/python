#프로그래밍 스터디 과제 (11.14)
#E 08) 다음 코드의 출력을 예상해보자.
x = 0
while (x < 100) :
    x += 2
print(x)
print()

#E 09) 다음 코드의 출력을 예상해보자.
n = 1349
sum = 0
while n > 0 :
    digit = n % 10
    sum += digit
    n = n//10
    print("합은 %d이고, 10으로 나누었을 때, 몫은 %d이다."%(sum, n))
print()

#E 10) 다음 중첩 루프의 실행 결과는 무엇일까?
numbers = [10,20]
items = ["TV","Phone"]
for x in numbers :
    for y in items :
        print(x,y)
print()

#P 01) 2부터 50사이의 모든 짝수를 출력하는 반복 루프를 작성한다.
#       for문
for i in range(2,51) :
    if i % 2 == 0 :
        print(i, end = " ")
print()
print()

#       while문
i = 2
while i <= 50 :
    if i % 2 == 0 :
        print(i, end = " ")
    i += 1
print()
