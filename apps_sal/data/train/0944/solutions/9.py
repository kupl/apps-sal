#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys;input = sys.stdin.readline
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]

for _ in range(inp()):
    n = inp()
    x = ip()
    par = [i%2 for i in x]
    pre = [0]*(n+1)
    prepar = [0]*(n+1)
    dt = {}
    for i in range(n):
        pre[i+1] = pre[i]+x[i]
        prepar[i+1] = prepar[i]+par[i]
        t = dt.get(x[i],[])
        t.append(i)
        dt[x[i]] = t
    #print(x)
    #print(pre)
    #print(dt)
    ans = 0
    for i in range(n):
        if len(dt[x[i]]) > 1:
            a,b = dt[x[i]][:2]
            dt[x[i]] = dt[x[i]][1:]
            if a == b: continue
            t = pre[b]-pre[a+1]
            ct = prepar[b]-pre[a+1]
            if x[i]%2:
                if ct%2:
                    ans = max(ans,t)
            else:
                if ((b-1-a+1+1)-ct)%2 == 0:
                    ans = max(ans,t)
    print(ans)

