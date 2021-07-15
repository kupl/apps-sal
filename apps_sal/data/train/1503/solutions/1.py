# cook your dish here

import math
t=int(input())

for i in range(t):
 n,m=list(map(int,input().split()))
 
 print(n//math.gcd(n,m)*m//math.gcd(n,m))
 

