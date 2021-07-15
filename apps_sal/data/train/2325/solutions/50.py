s=list(input())
t=list(input())

s=[0]+[1 if si=='A' else 2 for si in s]
t=[0]+ [1 if ti=='A' else 2 for ti in t]
import numpy as np
s=np.array(s)
t=np.array(t)
s=np.cumsum(s)
t=np.cumsum(t)
q=int(input())
for _ in range(q):
    a,b,c,d=list(map(int, input().split()))
    a-=1;c-=1
    test=s[b]-s[a]-t[d]+t[c]
    test%=3
    if not test:
        print('YES')
    else:
        print('NO')

