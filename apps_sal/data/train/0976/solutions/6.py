# dt = {} for i in x: dt[i] = dt.get(i,0)+1
#dt = {k:v for k,v in sorted(x.items(), key=lambda i: i[1])}
def ipnl(n): return [int(input()) for _ in range(n)]


def inp(): return int(input())
def ip(): return [int(w) for w in input().split()]


n = inp()
x = ip()
brac, ind = [], []
dt = {2: 0, 4: 0}
for i in range(n):
    if x[i] in [1, 3]:
        brac.append(x[i])
        ind.append(i)
        continue
    dt[x[i]] = max(dt[x[i]], i - ind[-1] + 1)
    ind.pop()
    brac.pop()
alt = 0
brac, depth = [], []
for i in range(n):
    if (x[i] == 1 or x[i] == 3) and brac == []:
        brac.append(x[i])
        depth.append(1)
        alt = max(alt, depth[-1])
    elif x[i] * brac[-1] == 3:
        brac.append(x[i])
        depth.append(depth[-1] + 1)
        alt = max(alt, depth[-1])
    elif x[i] == 1 or x[i] == 3:
        brac.append(x[i])
        depth.append(depth[-1])
        alt = max(alt, depth[-1])
    elif x[i] == 2 or x[i] == 4:
        brac.pop()
        depth.pop()

print(alt, dt[2], dt[4])
