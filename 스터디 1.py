#프로그래밍 스터디 과제 (11.14)
#01) if문과 while문을 비교하여 보라. 조건식이 같다면 어떻게 동작하는가
n = int(input("정수를 입력하시오. "))
if n < 10 :
    print("*"*n)
else :
    print("-"*20) # 주어진 수로부터만 조건식에 따라 결과를 도출한다.
print()

n = int(input("정수를 입력하시오. "))
while n < 10 :
    n += 1
    print("*"*n) # 주어진 수부터 조건식에 맞지 않는 수에 도달할 때까지 결과를 도출한다.
print()
    
    
#02) 구구단 출력 프로그램
dan = int(input("원하는 단은 : "))
i = 1

while i <= 9 :
    print("%d * %d = %d"%(dan, i, dan*i))
    i = i + 1
print()

#03) for문과 range() 함수를 사용하여 위의 문제를 다시 작성해보라.
dan = int(input("원하는 단은 : "))
for i in range(1,10) :
    result = dan*i
    print("%d * %d = %d"%(dan, i, result))
print()

#04) while문으로 1~n까지의 합계 구하기
n = int(input("정수를 입력하시오. : "))
hap = 0
i = 1
while i <= n :
    hap += i
    i += 1
print("%d까지의 합은 %d이다."%(n, hap))
