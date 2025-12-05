CLASS CALCULATOR
def__init__(self,a,b):
self.a=a
self.b=b

def add(self):
  print(self.a+seld.b)

def sub(self):
  print(self-self.b)

def mul(self):
  print(self.a*self.b)

def div(self):
  print(self.a/self.b)
#p1=calculator(a,b)
#p1.add()
#p1mul.()
print("""select your choice
1. for add
2. for sub
3. for mul
4. for div
""")
x= int(input("Enter your choice:"))
a= int(input("Enter first number"))
b= int(input("Enter second number"))

p1=calculator(a,b)
if(x==1):
  p1.addd()
elif(x==2):
  p1.sub()
elif(x==3):
  p1.mul()
elif(x==4):
  p1.div()
else:
  print("Enter proper choice")
