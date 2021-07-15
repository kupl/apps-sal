import itertools
t=int(input())
for i in range(t):
    n=int(input())
    a=[int(a) for a in input().split()]
    a.sort()
    print(a[len(a)-1]*a[len(a)-2],a[0]*a[1])
