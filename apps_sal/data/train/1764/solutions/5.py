from functools import lru_cache

@lru_cache(None)
def T(n,k):
    return 0 if n==0 or k==0 else T(n-1,k-1)+1+T(n-1,k)

def solve(e):
    d={0:False}
    floormax=0
    while e.eggs>0 and e.drops>0:
        n=floormax+1+T(e.drops-1,e.eggs-1)
        d[n]=t=e.drop(n)
        if not t:floormax=n
    return min([k for k,v in d.items() if v])
