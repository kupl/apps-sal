# cook your dish here
import math

for _ in range(int(input())):
 n,d=list(map(int,input().split(' ')))
 l= list(map(int, input().split(' ')))
 l1=[]
 l2=[]
 
 for i in l:
  if i>=80 or i<=9:
   l1.append(i)
  else:
   l2.append(i)
   
 x=math.ceil(len(l1)/d)
 y=math.ceil(len(l2)/d)
 
 print(x+y)
   
  



# 2
# 10 1
# 10 20 30 40 50 60 90 80 100 1
# 5 2
# 9 80 27 72 79
# Example Output
# 10
# 3  

