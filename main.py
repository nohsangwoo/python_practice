x="노상우는"
y=1989
z= "년에 태어났다"

# 캐스팅을 해주면 됨
print(x,str(y),z)


# boolean 사용법 : 첫글자가 대문자임
x=True
y=False
print(x,y)

if 2>1:
  print("hello")


if not 1>2:
  print("작동?")


# 조건이 전부True면 실행
if 1>0 and 2>1:
  print("and 사용법")

# 조건중 하나만 True라도 실행
if(1<0 or 2>1):
  print("or 사용법")


x=3

if x>5:
  print("hello")
elif x==3:
  print("Bye")
else:
  print("hi")