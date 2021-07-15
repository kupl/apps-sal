import sys
from math import *
from fractions import gcd
readints=lambda:map(int, input().strip('\n').split())
 
 
def ispal(s):
    n=len(s)
    for i in range(n//2):
        if s[i]!=s[n-i-1]:
            return False
    return True
 
s=input()
n=len(s)
 
 
    
 
for i in range(1,n):
    a,b=s[:i],s[i:]
    t=b+a
    if t!=s and ispal(t):
        print(1)
        return
 
 
k=n/2
if n%2==1:
    k=ceil(k)
 
 
k=int(k)
        
for i in range(1,k):
    a,b,c=s[:i],s[i:-i],s[-i:]
    t=c+b+a
    if t!=s and ispal(t):
        print(2)
        return
 
 
 
print("Impossible")
