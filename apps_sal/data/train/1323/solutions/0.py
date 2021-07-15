#for _ in range(int(input())):
#n,m = map(int,input().split())
#n = int(input())
#x = [int(w) for w in input().split()]
#x = [int(input()) for _ in range(n)]
#for i in range(n):
#dt = {} for i in x:dt[i] = dt.get(i,0)+1
#dt = {k:v for k,v in sorted(x.items(), key=lambda i: i[1])}

from bisect import bisect_left as bs
n = int(input())
x = [int(input()) for _ in range(n)]
dp = []
mn = float('inf')
idx = []
mlen = float('-inf')
si,sj = 0,0
sm = 0
def check(_sm,ind1,ind2,f):
    nonlocal mn,si,sj,mlen
    if _sm<abs(mn) or (_sm==abs(mn) and (idx[ind2]-idx[ind1])>mlen):
        si,sj = idx[ind1]+1,idx[ind2]
        mn = _sm*f
        mlen = sj-si+1

for k,v in enumerate(x,1):
    sm += v
    ind = bs(dp,sm)
    dp.insert(ind,sm)
    idx.insert(ind,k)
    check(abs(sm),0,ind,1)

    if ind>0:
        prev = ind-1
        diff = dp[ind]-dp[prev]
        while prev>0 and (dp[ind]-dp[prev-1])==diff:
            prev -= 1
        check(diff,prev,ind,1)
    if ind < len(dp)-1:
        nxt = ind+1
        diff = dp[nxt]-dp[ind]
        while nxt<len(dp)-1 and (dp[nxt+1]-dp[ind])==diff:
            nxt += 1
        check(diff,nxt,ind,-1)
print(mn)
print(si,sj)

