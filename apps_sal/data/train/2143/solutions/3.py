n,c,d = list(map(int, input().split()))
a = []
inf = 10 ** 10
for i in range(n):
    a.append(input().split())
    a[i][0], a[i][1] = int(a[i][0]), int(a[i][1])
    
def tr(r,s,have):
    if len(r) < 2:
        return 0
    mn = [0] * len(r)
    mn[0] = r[0][1]
    for i in range(len(r)):
        mn[i] = max(r[i][1], mn[i - 1])
    p = -1
    rs = -inf
    for i in range(len(r) - 1, -1, -1):
        while p + 1 < i and r[p + 1][0] <= have - r[i][0]:
            p += 1
        if p != -1:
            if p >= i:
                if i:
                    rs = max(rs, mn[i - 1] + r[i][1])
            else:
                rs = max(rs, mn[p] + r[i][1])
    return rs
        
        
        
    
    

ans = 0
cmx = 0
dmx = 0
for i in range(n):
    if a[i][2] == "C" and a[i][1] <= c:
        cmx = max(cmx, a[i][0])
    elif a[i][1] <= d:
        dmx = max(dmx, a[i][0])
if cmx > 0 and dmx > 0:
    ans = max(ans, cmx + dmx)
dm = []
for i in range(len(a)):
    if a[i][2] == "C":
        dm.append((a[i][1], a[i][0]))
dm.sort()
ans = max(ans,tr(dm,"C",c))
dm = []
for i in range(len(a)):
    if a[i][2] == "D":
        dm.append((a[i][1], a[i][0]))
dm.sort()
ans = max(ans,tr(dm,"D",d))
if ans == -inf:
    print(0)
else:
    print(ans)

    
    

