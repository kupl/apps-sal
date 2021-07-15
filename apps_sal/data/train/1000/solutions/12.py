# cook your dish here
T=int(input())
from math import ceil
for _ in range(T):
    n=int(input())
    arr=list(map(int,input().split()))
    min1=min(arr)
    x=ceil(n/min1)
    print(x)

