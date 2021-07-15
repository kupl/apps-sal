import functools
import math
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    g_1=functools.reduce(math.gcd,l)
    if g_1==1:
        print(-1)
        continue
    t_1=int(math.sqrt(g_1))
    c=0
    for i in range(2,t_1+2):
        if g_1%i==0:
            c=i
            break
    if c==0:
        print(g_1)
    else:
        print(c)
