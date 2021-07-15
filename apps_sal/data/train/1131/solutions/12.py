# cook your dish here
from collections import Counter

for j in range(int(input())):
    n,k = map(int,input().split())
    a=[int(x) for x in input().split()]
    z=Counter(a)
    p=[]
    for i in z:
        if z[i]>k:
            p.append(i)
    print(*sorted(p))
