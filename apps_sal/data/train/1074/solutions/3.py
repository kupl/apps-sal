import collections
def solve(n,l):
    c=0
    d=collections.Counter(l)
    for i in d:
        if d[i]>=2:
            c+=d[i]//2
    return c//2     
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(solve(n,l))

