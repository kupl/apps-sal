# cook your dish here
import sys
t = int(input())
for _ in range(t):
    N,k = map(int,input().split())
    A = list(map(int,input().split()))
    B = A*k
    max_ = -(sys.maxsize)-1
    value = 0
    for i in range(len(B)):
        value = value + B[i]
        if value>max_:
            max_ = value
        if value<0:
            value = 0
    print(max_)
