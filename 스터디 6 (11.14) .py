#프로그래밍 스터디 과제 (11.14)
# 05) 중첩 반복문을 사용하여서 다음과 같이 출력하는 프로그램을 작성하여 보자,
#       중첩 for문
n = int(input("정수를 입력하시오: "))
for i in range(1, n+1) :
    for j in range(1, i+1) :
        print(j, end= " ")
    print()
print()
#       중첩 while문
n = int(input("정수를 입력하시오: "))
i = 1
while i <= n :
    j = 1
    while j <= i :
        print(j, end = " ")
        j += 1
    print()
    i += 1
print()

# 10번) 1^2 + 2^2 + ... + n^2의 값을 출력하여 보자.
#       for문
n = int(input("n의 값을 입력하시오: "))
hap = 0
for i in range(1,n+1) :
    hap += i**2
print("계산값은 %d입니다."%hap)
print()

#       while문
n = int(input("n의 값을 입력하시오: "))
hap = 0
i = 1
while i <= n :
    hap += i**2
    i += 1
print("계산값은 %d입니다."%hap)
