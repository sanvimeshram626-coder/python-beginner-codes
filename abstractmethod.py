from abc import ABC, abstract method
class G_S(ABC):
  def__init__(self,r):
  self.r=r

@abstractmethod
def area(self,a):
  pass
def per(self,a):
  pass

class circle(G_S):
  def area(self,a)
  print(3.14*a*a)
 def per(self,a):
  print(2*3.14*a)

class rec(G_S):
  def__init__(self,a,b):
  G_S.__init__(self,a)
  self.b=b
  def per(self,a,b):
    print("rec perimeter",2*(a+b))
  def area(self,a,b):
    print("rec area",a*b)

p1=circle(5)
p1.area(5)
p1.per(5)
p2=rec(2,3)
p2.area(2,3)
p2.per(2,3)
