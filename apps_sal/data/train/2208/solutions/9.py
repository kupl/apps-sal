import sys
n, k = [int(i) for i in sys.stdin.readline().split()]
gwl = []
for i in range(n + 1):
    gwl.append([])
data = []
for kk in range(k):
    d = [int(i) for i in sys.stdin.readline().split()]
    gwl[d[0]].append(kk)
    gwl[d[1]].append(kk)
    data.append(d)

one = set()
two = set(range(k))
sn = [1] * (n + 1)
doub = [1] * k
ans = 0


while True:
    if one:
        ans += 1
        q = one.pop()
        d = data[q]
        if sn[d[0]]:
            sn[d[0]] = 0
            for oth in gwl[d[0]]:
                if doub[oth]:
                    two.remove(oth)
                    one.add(oth)
                    doub[oth] = 0
                else:
                    one.discard(oth)
        else:
            sn[d[1]] = 0
            for oth in gwl[d[1]]:
                if doub[oth]:
                    two.remove(oth)
                    one.add(oth)
                    doub[oth] = 0
                else:
                    one.discard(oth)
    elif two:
        ans += 1
        q = two.pop()
        doub[q] = 0
        d = data[q]
        for w in range(2):
            sn[d[w]] = 0
            for oth in gwl[d[w]]:
                if doub[oth]:
                    two.remove(oth)
                    one.add(oth)
                    doub[oth] = 0
                else:
                    one.discard(oth)
    else:
        break
print(k - ans)
