from math import gcd,sqrt
def ii():return int(input())
def mi():return map(int,input().split())
def li():return list(mi())
def si():return input()
t=ii()
while(t):
 t-=1
 n=ii()
 n*=24
 x,y,z=mi()
 s=gcd(x,y)
 s1=(x*y)//s
 s=gcd(s1,z)
 s1=(s1*z)//s
 print(n//s1)
