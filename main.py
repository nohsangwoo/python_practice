x="노상우는"
y=1989
z= "년에 태어났다"

# 캐스팅을 해주면 됨
print(x,str(y),z)
# ---------------------------------------------------------------

# boolean 사용법 : 첫글자가 대문자임
x=True
y=False
print(x,y)

# ---------------------------------------------------------------
if 2>1:
  print("hello")


if not 1>2:
  print("작동?")


# ---------------------------------------------------------------
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

  # ---------------------------------------------------------------

  #function

def chat(name1,name2,age):
  print("%s: 안녕? 넌 몇 살이니?" % name1)
  print("%s: 나?;;; 나는 %d" % (name2, age))


chat("알렉스","영희" ,20)

#---------------------------------------------------------

def dsum(a,b):
  result = a+b
  return result

print(dsum(10,20))



#-------------------------------------------------------------------------------------
# 먼저 이름과 나이를 받아라
# 나이가 10살 미만이면 "안녕" 이라고 말해라
# 나이가 10살에서 20살 사이면 "안녕하세요" 라고 말해라
# 그 외에는 "안녕 하십니까" 라고 말해라

def sayHello(name,age):
  if(age<10):
    print("안녕 " + name)
  elif(10<age and age<20):
    print("안녕하세요 " + name)
  else:
    print("안녕 하십니까 " + name)

sayHello("상우",8)
  


#--------------------------------------------------------

#for, while 사용법

# 1. for
for i in range(0):
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 오빠 죄송한데 말걸지 말아주시겠어요? 차단할께요")

# 2. while
i=4
while i<3:
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 오빠 죄송한데 말걸지 말아주시겠어요? 차단할께요")
  i+=1



# 3. break, continue
i=4
while True:
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 오빠 죄송한데 말걸지 말아주시겠어요? 차단할께요")
  i+=1
  if i >2:
    break



# 4. continue
i=0
for i in range(3):
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 오빠 죄송한데 말걸지 말아주시겠어요? 차단할께요")
  continue
  print("저기 영희야? 밥 먹었어?")
