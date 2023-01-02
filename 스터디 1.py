# 08
x = 0
while x < 100 :
    x += 2
print(x)


# 10
n = [10, 20]
i = ["TV", "Phone"]
for x in n :
    for y in i :
        print(x,y)


# P.198 Programming
# 01 (for문)
for i in range(2, 51, 2) :
    print(i, end = " ")
    
# 01 (while문)
i = 2
while i < 51 :
    print(i, end = " ")
    i += 2


# 02
mylist = [11, 22, 23, 99, 81, 93, 35]
hap = 0
for x in mylist :
    hap += x
print("정수의 합은 %d"%hap)


# 03 (for문)
hap = 0
for i in range(1, 101) :
    if i % 3 == 0 :
        hap += i
print("1부터 100 사이의 모든 3의 배수의 합은 %d입니다."%hap)

# 03 (while문)
hap = 0
i = 1
while i < 101 :
    if i % 3 == 0 :
        hap += i
    i += 1
print("1부터 100 사이의 모든 3의 배수의 합은 %d입니다."%hap)


#04
n = int(input("정수를 입력하시오. : "))
print("약수 : ", end = " ")
for i in range(1, n+1) :
    if n % i == 0 :
        print(i, end = " ")


# 05 (for문)
n = int(input("정수를 입력하시오 : "))
for i in range(1, n+1) :
    for j in range(1, i+1) :
        print(j, end = " ")
    print()

# 05 (while문)
n = int(input("정수를 입력하시오. : "))
i = 1
while i < n+1 :
    j = 1
    while j < i + 1 :
        print(j, end = " ")
        j += 1
    i += 1
    print()


# 10 (for문)
n = int(input("n의 값을 입력하시오. : "))
hap = 0
for i in range(1, n+1) :
    hap += i ** 2
print("계산값은 %d입니다."%hap)

# 10 (while문)
n = int(input("n의 값을 입력하시오. : "))
i = 1
hap = 0
while i <= n :
    hap += i ** 2
    i += 1
print("계산값은 %d입니다."%hap)
