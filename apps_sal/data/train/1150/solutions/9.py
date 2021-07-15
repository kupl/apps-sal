# cook your dish here
import math
for _ in range(int(input())):
 n=int(input())
 s=0
 while n!=0:
  s+=1
  n-=(int(math.sqrt(n)))**2
 print(s)
