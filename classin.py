CLASS IN
class college:
  def college_name(self):
    print("college:RBU University, Nagpur")

class club(college):
  pass
  class event(college):
    def event_name(self):
      print("hi")

s1= club()
s2= event()

s1.college_name()
s2.college_name()
s2.event_name()
