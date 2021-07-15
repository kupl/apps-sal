import math
t=int(input())
for i in range(t):
 (N,M)=map(int,input().split(' '))
 x=math.gcd(N,M)
 y=((N*M)//(x**2))
 print(y)
