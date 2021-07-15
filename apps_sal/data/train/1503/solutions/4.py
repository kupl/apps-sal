import math
n=int(input())
x=[]
for i in range(0,n):
 l,b=list(map(int, input().split()))
 area=l*b
 g=math.gcd(l,b)
 g=g**2
 x.append(area//g)
for i in x:
 print(i)

