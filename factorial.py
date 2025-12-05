FACTORIAL
num= int(input("Enter number to find the factorial"))
if(num==1):
  print("factorial of 1 is 1")
elif (num<0):
  print("not possible")
else:
  n= num-1
  while (n>0):
    num= num*n
    n= n-1
    print(num)
