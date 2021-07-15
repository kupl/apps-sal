from math import sqrt
for _ in range(int(input())):
    n=int(input())
    l=[0]*n
    c=0
    for i in range(n):
        l[i]=list(map(int,input().split()))
        c=c+l[i].count(0)
    q=c//2
    a=(-1+sqrt(1+8*q))//2
    print(int(n-a-1))
