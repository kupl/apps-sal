import bisect


def wormholes(tlist, vlist, wlist):
    sumlist = []
    for i in range(len(tlist)):
        if tlist[i][0] not in vlist:
            x = bisect.bisect_left(vlist, tlist[i][0])
            x = x - 1
            if x < 0:
                continue
        else:
            x = vlist.index(tlist[i][0])
        if tlist[i][1] not in wlist:
            y = bisect.bisect_right(wlist, tlist[i][1])
            if y >= len(wlist):
                continue
        else:
            y = wlist.index(tlist[i][1])
        sumlist.append(wlist[y] - vlist[x] + 1)
    return min(sumlist)


(n, x, y) = input().split()
(n, x, y) = (int(n), int(x), int(y))
timelist = []
for i in range(n):
    (s, e) = input().split()
    (s, e) = (int(s), int(e))
    timelist.append([s, e])
v = list(map(int, input().strip().split()))
w = list(map(int, input().strip().split()))
v.sort()
w.sort()
miv = min(v)
maw = max(w)
for i in range(n):
    if timelist[i][0] < miv or timelist[i][1] > maw:
        timelist[i] = [0, 0]
while [0, 0] in timelist:
    timelist.remove([0, 0])
print(wormholes(timelist, v, w))
