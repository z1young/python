#프로그래밍 스터디 과제 (11.14)
#P 02) 다음 리스트에 저장된 정수들의 합을 계산하는 프로그램을 작성해보자.
#       for문
myList = [11,22,23,99,81,93,35]
hap = 0
for i in myList :
    hap += i
print("정수들의 합은 %d"%hap)
print()

#P 03) 1부터 100사이의 모든 3의 배수의 합을 계산하여 출력하는 프로그램을 작성하라
#       for문
hap = 0
for i in range(1,101) :
    if i % 3 == 0 :
        hap += i
print("1부터 100사이의 모든 3의 배수의 합은 %d입니다."%hap)
print()
#       while문
hap = 0
i = 1
while i <= 100 :
    if i % 3 == 0 :
        hap += i
    i += 1
print("1부터 100사이의 모든 3의 배수의 합은 %d입니다."%hap)
print()

#P 04) 사용자가 입력한 정수의 모든 약수를 화면에 출력하는 프로그램을 작성하라.
#       for문
n = int(input("정수를 입력하시오: "))
for i in range(1,n+1) :
    if n % i == 0 :
        print(i, end = " ")
print()
print()
#       while문
n = int(input("정수를 입력하시오: "))
i = 1
while i <= n :
    if n % i == 0 :
        print(i, end = " ")
    i += 1
print()
