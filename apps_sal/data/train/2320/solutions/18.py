import sys,math,string,bisect
input=sys.stdin.readline
from collections import deque
L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split())
M=lambda : list(map(int,input().split()))
I=lambda :int(input())
n=I()
l=L()
m=L()
x=[]
for i in range(n):
    x.append([-m[i],i])
x.sort(key=lambda x:x[0])
x=x[-1::-1]
l.sort(reverse=True)
d=[0]*n
for i in range(n):
    d[x[i][1]]=l[i]
print(*d)


