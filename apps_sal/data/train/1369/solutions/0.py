from math import sqrt 

test = int(input())
for i in range(test):
 sum = 0
 max = int(input())
 if max==1:
  sum = 0
 elif max==2:
  sum += 2
 else:    
  sum = sum + 2
  for x in range(3,max+1):
   half = int(sqrt(x)) + 1
   if all(x%y!=0 for y in range(2,half)):
    sum = sum + x
 print(sum) 
