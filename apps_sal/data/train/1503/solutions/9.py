import math
t=int(input())
for i in range(t):
 n,m=map(int,input().split())
 x=math.gcd(n,m)
 ans=(n*m)//(x*x)
 print(ans)
