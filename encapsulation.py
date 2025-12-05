class test:
  #private variable
  __data= 40

#public method to access private variable
def show_data(self):
  print("Data id:",self.__datat)

#create object
ex=test()

#accessing private variable directly --> error
#print(ex.__data) ---> attribute error

#access it through public method is allowed
ex.show_data()
s1=club()
s2=event()

s1.college_name()
s2.college_name()
s2.event_name()
