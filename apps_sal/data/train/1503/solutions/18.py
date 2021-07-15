# cook your dish here
import math
t = int(input())
for i in range(t):
 l,b = map(int, input().split())
 r = l*b
 s = math.gcd(l,b)
 s=s**2
 print(r//s)
