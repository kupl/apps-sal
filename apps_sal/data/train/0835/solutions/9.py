# cook your code here
t = int(input().strip())

while t > 0 :
 t = t - 1
 a , b = [ int(x.strip()) for x in input().split() ]
 

 if (a*b)%2 == 0 and a != 1 and b != 1 : 
  print("Yes")
 elif ( a == 1 or b == 1 ) and a*b == 2 :
  print("Yes")
 else: 
  print("No")
