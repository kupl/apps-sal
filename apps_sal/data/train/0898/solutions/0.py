# cook your dish here
from math import pow
t = int(input())
for _ in range(t):
    m,n = map(int,input().rstrip().split())
    cnt = len(str(n))
    x = pow(10,cnt)
    if n == x-1:
        print(m*cnt,m)
    else:
        print(m*(cnt-1),m)
