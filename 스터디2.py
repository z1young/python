 #02 (for 반복문 사용)
import turtle as t
t.shape("turtle")
t.color("purple")
for i in range(4):
    t.forward(40)
    t.left(90)
t.done
 #03 (for 반복문 사용)
import turtle as t
t.shape("turtle")
t.color("orange")
for i in range(6):
    t. forward(80)
    t.left(60)
t.done

#p.55 programming 예제
 #01
print("환영합니다.")
print("파이썬의 세계로 오신것을 환영합니다.")
print("파이썬은 강력합니다.")
 #01 (\n : 줄바꿈)
print("환영합니다. \n파이썬의 세계로 오신 것을 환영합니다. \n파이썬은 강력합니다.")
 #02
print("+","="*16,"+")
print("|"," "*4,"홍길동"," "*4,"|")
print("+","="*16,"+")
 #03
print(1+2+3)
 #04
a=1+2+3
print(f"1+2+3을 계산하면 {a}입니다.")
 #05 (for 반복문, forward(), right(), left() 사용)
import turtle as t
t.shape("turtle")
t.color("green")
t.forward(40)
t.left(90)
for i in range(2):
    t.forward(40)
    t.right(90)
t.forward(40)
t.left(90)
t.forward(40)
t.done()
