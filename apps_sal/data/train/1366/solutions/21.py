import numpy as np
t=int(input())
l=[]
for i in range(t):
    n=int(input())
    a = list(map(int,input().rstrip().split()))
    a=np.trim_zeros(a)
    if len(a)>0:
        l.append(len(a))
    else:
        l.append(1)
for x in range(t):
    print(l[x])

