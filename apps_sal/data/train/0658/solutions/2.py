#dt = {} for i in x: dt[i] = dt.get(i,0)+1
#dt = {k:v for k,v in sorted(x.items(), key=lambda i: i[1])}
ipnl = lambda n: [int(input()) for _ in range(n)]
inp = lambda :int(input())
ip = lambda :[int(w) for w in input().split()]

for _ in range(inp()):
    n = inp()
    x = ip()
    up = [1]*(n+1)
    dn = [1]*(n+1)
    up[-1],dn[-1] = 0,0
    for i in reversed(list(range(n-1))):
        if x[i] <= x[i+1]:
            dn[i] += up[i+1]
        if x[i] >= x[i+1]:
            up[i] += dn[i+1]
    ans = 0
    for i in range(n):
        t = dn[i]
        if t%2:
            t += dn[i+t]
        else:
            t += up[i+t]
        ans = max(ans,t+1)
    print(ans)



