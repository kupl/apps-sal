# cook your dish here
from fractions import gcd
# def gcd(a,b):
#     if a==0:
#         return b
#     elif b==0:
#         return a
#     if a>=b:
#         return gcd(b,a/b)
#     else:
#         return gcd(b,a)
t=int(input())
while t:
    x,y=[int(i) for i in input().split(' ')]
    if gcd(x,y)==1:
        print("YES")
    else:
        print("NO")
    t-=1
