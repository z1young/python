#p.31
 # 01
print("안녕하세요")
   #파이썬은 대소문자를 구별하기 때문에 PRINT라고 작성한다면 이를 어떻게 처리해야하는 지 알지 못한다.
 #02
print("programming에 입문하신 것을 축하드립니다.")
 #05
print("생일축하"*10) # 문자열*숫자는 문자열이 숫자만큼 반복된다.
 #06
print("Hello")

#p.38
 #01
print("3*1=",3*1)#따옴표 안에 들어가 있는 텍스트는 문자열 그대로 출력된다.
print("3*2=",3*2)
print("3*3=",3*3)

#p.39
print("*"*30)
print("print()를 사용한 예제입니다.")
print("내가 제일 좋아하는 숫자는 7입니다.")
print("*"*30)

#p.49 중간점검
 #01 (for 반복문 사용)
import turtle as t
t.shape("turtle")
t.color("red")
for i in range(3):
    t.forward(30)
    t.left(120)
t.done
 #01
import turtle as t
t.shape("turtle")
t.color("green")

t.forward(60)
t.left(120)
t.forward(60)
t.left(120)
t.forward(60)

turtle.mainloop()
turtle.bye()

