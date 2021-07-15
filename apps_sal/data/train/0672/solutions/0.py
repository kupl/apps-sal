# cook your dish here
from math import sqrt
for i in range(int(input())):
 x1,y1,x2,y2=list(map(float,input().split()))
 m=(y2-y1)/(x2-x1)
 c=y2-m*x2
 print('Test case : ',i+1)
 q=int(input())
 for i in range(q):
  x3,y3=list(map(float,input().split()))
  if(y3-m*x3-c==0):
   print("YES")
  else:
   d=(abs(y3-m*x3-c))/sqrt(1+m*m)
   print("NO")
   print("%.6f" % d)

