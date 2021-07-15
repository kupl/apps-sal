#dt = {} for i in x: dt[i] = dt.get(i,0)+1
#dt = {k:v for k,v in sorted(x.items(), key=lambda i: i[1])}
ipnl = lambda n: [int(input()) for _ in range(n)]
inp = lambda :int(input())
ip = lambda :[int(w) for w in input().split()]

for _ in range(inp()):
    n = inp()
    sco = [0]*n
    x,y = [],[]
    for i in range(n):
        a,b = ip()
        x.append([a,i])
        y.append([b,i])
    x.sort(reverse = True,key = lambda i: i[0])
    y.sort(key = lambda i: i[0])
    for i in range(n):
        sco[x[i][1]] += i
        sco[y[i][1]] += i
    print(*sco)




