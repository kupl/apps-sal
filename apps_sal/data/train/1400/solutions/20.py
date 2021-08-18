minm = 0
maxm = 0
minmlist = []
maxmlist = []
t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    for i in range(l):
        a = 2**(i)
        minm += a
    minm += n - l
    for j in range(r):
        b = 2**(j)
        maxm += b
    maxm += (n - r) * (2**(r - 1))
    minmlist.append(minm)
    maxmlist.append(maxm)
    minm = 0
    maxm = 0
for k in range(t):
    print(minmlist[k], maxmlist[k])
