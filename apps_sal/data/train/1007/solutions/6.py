# cook your dish here
import math
t=int(input())
for i in range(0,t):
 n=int(input())
 a=list(map(int, input().split()))
 c=a[0]
 for j in range(1,len(a)):
  c=math.gcd(c,a[j])
 if c==1:
  print(n)
 else:
  print(-1)


