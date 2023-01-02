# P.244 Exercise
#01
def max(a,b) :
    if a > b :
        result = a
    else :
        result = b
    return result


# 02
def main() :
    print(mistery(10,20))
def mistery(a,b) :
    result = a
    if b < result :
        result = b
    return result
main()


# 03
def sub(a, b, c, d) :
    pass
def sub(1, 2, 3, d=4) :
    pass


# 04
def mistery(a, b, min) :
    min = a
    if b < min :
        min = b
min = 0
mistery(20, 10, min)
print(min)


# 05
x = 10
def dec() :
    global x
    x = x - 1
dec()
print(x)


# 06
x = int(input("정수를 입력하시오. : "))
if x < 0 :
    y = 10
print(y)


# 07
def sub(a=, b=3 ) :
    print(a, b)


# 08
def sub(a, b) :
    return a+b, a-b
x, y = sub(10, 20)
print(x, y)


# 09
global = 0
def sub() :
    local = 1
    print(global)
    print(local)
sub()
print(global)
print(local)


# P.246 Programming
# 01
def get_peri(r = 5) :
    p = 2.0 * 3.141692 * r
    return p
print(get_peri())
print(get_peri(4.0))


# 02
def add(a, b) :
    return a + b
def minus(a, b) :
    return a - b
def multi(a, b) :
    return a * b
def div(a, b) :
    return a / b

a = int(input("첫번째 정수를 입력하시오. : "))
b = int(input("두번째 정수를 입력하시오. : "))
print("%d + %d = %d"%(a, b, add(a,b)))
print("%d - %d = %d"%(a, b, minus(a,b)))
print("%d * %d = %d"%(a, b, multi(a,b)))
print("%d / %d = %d"%(a, b, div(a,b)))


# 03
def calc(a, b) :
    return a+b, a-b, a*b, a/b
x = int(input("첫번째 정수를 입력하시오. : "))
y = int(input("두번째 정수를 입력하시오. : "))
a,b,c,d = calc(x,y)
print(a, b, c, d, "이 반환되었습니다.")


# 04
def getGrade(score) :
    if score >= 90 :
        print("성적은 A입니다.")
    elif score >= 80 :
        print("성적은 B입니다.")
    elif score >= 70 :
        print("성적은 C입니다.")
    elif score >= 60 :
        print("성적은 D입니다.")
    else :
        print("성적은 F입니다.")
score = eval(input("점수를 입력하세요. : "))
getGrade(score)


# 06
def add(a, b) :
    return a + b
a = int(input("첫 번째 정수를 입력하시오. : "))
b = int(input("두 번째 정수를 입력하시오. : "))
print("정수 %d + %d의 합은 %d"%(a, b, add(a,b)))
