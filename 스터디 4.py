# P.213
def main() :
    print("20cm 피자 2개의 면적 : ", get_area(20) + get_area(20))
    print("30cm 피자 1개의 면적 : ", get_area(30))
def get_area(r) :
    if r > 0 :
        area = 3.14 * r ** 2
    else :
        area = 0
    return area
main()

# P.222
def f(x) :
    return x**2 -x -1
def b_m(a,b,error) :
    if f(a) * f(b) > 0 :
        print("구간에서 근을 찾을 수 없습니다.")
    else :
        while (b - a) / 2.0 > error :
            midpoint = (a + b) / 2.0
            if f(midpoint) == 0 :
                return(midpoint)
            elif f(a) * f(midpoint) < 0 :
                b = midpoint
            else :
                a = midpoint
        return midpoint
answer = b_m(1, 2, 0.0001)
print("x ** 2 - x - 1의 근 : ",answer)


# P.223
def pay(r,h) :
    m = 0
    if h > 30 :
        m = r * 30 + 1.5 * r * (h-30)
    else :
        m = r * h
    return m

r = eval(input("시급을 입력하시오 : "))
h = eval(input("근무 시간을 입력하시오 : "))
print("주급은" + str(pay(r, h)))


# P.227
def get_info() :
    n = input("이름 : ")
    a = int(input("나이 : "))
    return n, a
name, age = get_info()
print("이름은",name,"이고 나이는",age,"살입니다.")


# P.231
import turtle as t
t.shpae("turtle")

def sqaure(l) :
    t.down()
    for i in range(4) :
        t.forward(l)
        t.left(90)
    t.up()
square(100)
t.forward(120)
square(100)
t.forward(120)
square(100)

t.done()


# P.241
import turtle as t
t.shape("turtle")
t.speed(0)

def f(x) :
    return x ** 2 + 1

t.goto(200,0)
t.goto(0, 0)
t.goto(200, 0)
t.goto(0, 0)

for x in range(150) :
    t.goto((x, int(0.01 * f(x)))
t.bye()
