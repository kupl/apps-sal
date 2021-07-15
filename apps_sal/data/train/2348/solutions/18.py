import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
x = list(map(int, input().split()))
l = int(input())
q = int(input())
ps = [None]*n
# ps2 = [None]*n
j = 0
for i in range(n):
    if j<i:
        j = i
    while j+1<n and x[j+1]-x[i]<=l:
        j += 1
    ps[i] = j
# ダブリング
def double(ps):
    # global: n=psのサイズ
    k = 0
    n = len(ps)
    while pow(2,k)<n:
        k += 1
    prev = [[None]*n for _ in range(k)] # ノードjから2^i個上の上司
    for j in range(n):
        prev[0][j] = ps[j]
    for i in range(1,k):
        for j in range(n):
            p = prev[i-1][j]
            if p>=0:
                prev[i][j] = prev[i-1][p]
            else:
                prev[i][j] = p
    return prev
dl = double(ps)
ans = [None]*q
def sub(a,b,x):
    for k in range(len(dl)-1, -1, -1):
        if x>=pow(2,k):
            x-=pow(2,k)
            a = dl[k][a]
    return a>=b
        
        
for i in range(q):
    a,b = map(lambda x: int(x)-1, input().split())
    a,b = min(a,b), max(a,b)
#     print(a,b)
    res = 0
    tmp = float("inf")
    l = 0
    r = n
    while l+1<r:
        m = (l+r)//2
        if sub(a,b,m):
            r = m
        else:
            l = m
    ans[i] = r
write("\n".join(map(str, ans)))
