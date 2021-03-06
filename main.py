

x="노상우는"
y=1989
z= "년에 태어났다"

# 캐스팅을 해주면 됨
print(x,str(y),z)

print("-------------------------------------------------------------------------")
# ---------------------------------------------------------------

# boolean 사용법 : 첫글자가 대문자임
x=True
y=False
print(x,y)
print("-------------------------------------------------------------------------")
# ---------------------------------------------------------------
if 2>1:
  print("hello")


if not 1>2:
  print("작동?")

print("-------------------------------------------------------------------------")
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
print("-------------------------------------------------------------------------")
  # ---------------------------------------------------------------

  #function

def chat(name1,name2,age):
  print("%s: 안녕? 넌 몇 살이니?" % name1)
  print("%s: 나?;;; 나는 %d" % (name2, age))


chat("알렉스","영희" ,20)
print("-------------------------------------------------------------------------")
#---------------------------------------------------------

def dsum(a,b):
  result = a+b
  return result

print(dsum(10,20))


print("-------------------------------------------------------------------------")
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
  

print("-------------------------------------------------------------------------")
#--------------------------------------------------------

#for, while 사용법

# 1. for
for i in range(0):
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 오빠 죄송한데 말걸지 말아주시겠어요? 차단할께요")

print("-------------------------------------------------------------------------")

# 2. while
i=4
while i<3:
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 오빠 죄송한데 말걸지 말아주시겠어요? 차단할께요")
  i+=1

print("-------------------------------------------------------------------------")

# 3. break, continue
i=4
while True:
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 오빠 죄송한데 말걸지 말아주시겠어요? 차단할께요")
  i+=1
  if i >2:
    break

print("-------------------------------------------------------------------------")

# 4. continue
i=3
for i in range(0):
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 오빠 죄송한데 말걸지 말아주시겠어요? 차단할께요")
  continue
  print("저기 영희야? 밥 먹었어?")

# https://www.youtube.com/watch?v=M6kQTpIqpLs
#37.21



print("-------------------------------------------------------------------------")
# 자료구조

# 1. List 사용법
print("#list 사용법---------")
x=list()
y=[1,2]
z=["hello","bye"]
a=["hello", 1 , 3.23]
print(x)
print(y)
print(z)
print(a)

print("-------------------------------------------------------------------------")
# 리스트 합치기
print("리스트합치기",x+z)


print("-------------------------------------------------------------------------")
# 리스트 바꾸기
print("리스트 바꾸기")
x = [1,2,3,4]
x[3] = 10
print(x)


print("-------------------------------------------------------------------------")
# 리스트 길이
print("리스트 길이")
print(len(x))


print("-------------------------------------------------------------------------")
# 리스트-정렬
print("리스트 정렬")
print(sorted(x))

print("-------------------------------------------------------------------------")
# 리스트 -  총합
print(  "리스트 총합")
print(sum(x))

print("-------------------------------------------------------------------------")
# 리스트 for문
print("list for 문")
x=[4,3,2,1]
for n in x:
  print(n)

print("-------------------------------------------------------------------------")
# 리스트 값으로 인덱스로 찾기
x=[1,3,5,7,8,9]
y=["hello","bye","good"]
print("리스트 값으로 인덱스를 찾기")
print(x.index(3))
print(y.index("hello"))


print("-------------------------------------------------------------------------")
# 리스트 안에 값이 있는지 여부
print("리스트 안에 값이 있는지 여부")
print("ty" in y)

if "hello" in y:
  print("hello가 있어요")


print("-------------------------------------------------------------------------")
print("Tuple 사용법")
# 튜플은 한번 설정해두면 바꿀수 없음 (mutable(가변) vs immutable(불변))

# Tuple
x=(1,2,3)
y=('a','b','c')
z=(1,"hello","three")

print(x+ y)
print("a" in y)
print(z.index(1))
print(x[0])

# 튜플은 업데이트 불가능
# x[0]=10 이런식으로 업데이트가 불가능




print("-------------------------------------------------------------------------")
print("dictionary 사용법")
# javascript의 object와 같은듯

x={
  "name":"상우",
  "age":33,
  0:"test",
  1:"one"
  }

y = {}

print(x)
print(x["name"])
print(x["age"])
print(x[0])
print(x[1])

print( "age" in x)

print("-------------------------------------------------------------------------")
# dictionary에 있는 모든 key를 보여주세요
print("dictionary에 있는 모든 key를 보여주세요")
print(x.keys())


print("-------------------------------------------------------------------------")
# dictionary에 있는 모든 value를 보여주세요
print("dictionary에 있는 모든 value를 보여주세요")
print(x.values())



print("-------------------------------------------------------------------------")
# dictionary를 이용한 for문 사용법
print("dictionary를 이용한 for문 사용법")
for key in x:
  print("key: "+ str(key))
  print("value", str(x[key]))


print("-------------------------------------------------------------------------")
# assignment
# 해당 키에 새로운값을 할당 가능(update)
x[0] = "real"
print(x)


print("-------------------------------------------------------------------------")
# 새로운 키와 새로운 값을 할당가능
x["school"] = "구지 초교"
print(x)


print("-------------------------------------------------------------------------")
# 자료구조 recap
print("과일 숫제 세는 프로그램 만들기")

fruits = ["사과","사과","바나나","바나나","딸기","키위","복숭아","복숭아","복숭아"]
# 과일 숫자 세는 프로그램 만들기
d={}
for fruit in fruits:
  if fruit in d: #"사과" 라는 key가 D라는 딕셔너리에 들어있어?
    d[fruit] =  d[fruit] + 1  #그럼 "사과" 갯수를 하나 올려줘 
  else:
    d[fruit] = 1 #만약 "사과" 라는 애가 없으면, 그걸 딕셔너리에 넣고 밸류는 1로 만들어줘


  
print(d)


print("-------------------------------------------------------------------------")
# 클래스 사요애법
print("class 사용법")


class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def say_hello(self, to_name ):
    print("안녕! " + to_name +  " 나는 " +  self.name)

  def introduce(self):
    print("내 이름은 " + self.name + "그리고 나는 " + str(self.age) + " 살이야" )

sangwoo = Person("sangwoo",33)
jongran = Person("jongran",59)


sangwoo.introduce()
sangwoo.say_hello("철수")

jongran.introduce()
jongran.say_hello("영희")


print("-------------------------------------------------------------------------")
# 상속 inheritance
print("상속 inheritance 사용법")


class Police(Person):
  def arrest(self, to_arrest):
    print("넌 체포됐다, " + to_arrest)

class Programmer(Person):
  def program(self, to_program):
    print("이번에 만들 프로그램은" + to_program)


jenny = Police("제니",20)
michael = Programmer("마이클",20)

jenny.introduce()
jenny.arrest("케이코")

michael.introduce()
michael.program("업그레이드된 매직미러 앱")


print("-------------------------------------------------------------------------")
# 모듈 OR 패키지 사용법
# animal package
# dog, cat modules
# dog, cat modules can say "hi"

print("모듈 OR 패키지 사용법")

from animal import dog # animal 패키지에서 dog라는 모듈을 갖고와줘
from animal import cat # animal 패키지에서 cat라는 모듈을 갖고와줘


d = dog.Dog() # instance
d.hi()

c = cat.Cat() # instance
c.hi()


from animal import * # animal 패키지가 갖고 있는 모듈을 다 불러와!
d = Dog()
c = Cat()

d.hi()
c.hi()


print("-------------------------------------------------------------------------")

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="sangwoo")
location = geolocator.geocode("Seoul, South Korea")
# 주소
print(location.address)
# 위도, 경도
print((location.latitude, location.longitude))
# location의 날것의 그대로를 다 가져와 달라
print(location.raw)


# https://www.youtube.com/watch?v=M6kQTpIqpLs
# 1시간 까지 봤음