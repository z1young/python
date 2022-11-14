#프로그래밍 스터디 과제 (11.14)
#08) break문이 반복문에서 실행되면 반복문을 빠져나온다.

#09) 다음 코드의 출력을 쓰시오.
for i in range(1,10,1) :
    if i % 3 == 0 : break
    print(i)
print()

#E 02) 다음의 프로그램에서 생성되는 출력 결과는 무엇인가?
i = 0
while i <= 8:
    print(i)
    i += 2
print()

#E 03) 다음의 프로그램에서 생성되는 출력 결과는 무엇인가?
i = -2
while i >= -5 :
    print(i, end = " ")
    i += -1
print()
print()

#E 04) 다음의 for루프를 while루프로 변환하라.
i = 0
sum = 0
while i <= 100 :
    sum += i
    i += 1
print("100까지의 합 = %d"%sum)

#E 05) 다음의 프로그램을 실행시키면 "Hello World!"는 몇 번이나 출력되는가?
for x in range(10) :
    if x > 5 : continue
    if x > 8 : break
    print("Hello World!")
print()

#E 06) 다음 코드의 출력을 예상해보자.
i = 0
while i < 10 :
    print(i)
    i += 1
print()

#E 07) 다음과 같은 소스 코드는 몇 번이나 반복하는가?
i = 0
while i <= 10 :
    print("Hi!")
    i += 1
