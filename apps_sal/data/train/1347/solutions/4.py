import operator
n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
h = [0] * 100001
for x in a:
    h[x] = 1
ss = {}
ns = {}

while m:
    m -= 1
    f, p, s = [x for x in input().split()]
    f = int(f)
    p = int(p)
    if h[f] == 1:
        ss[p] = [f, s]
    else:
        ns[p] = [f, s]

ss = sorted(list(ss.items()), key=operator.itemgetter(0), reverse=True)
ns = sorted(list(ns.items()), key=operator.itemgetter(0), reverse=True)
for x in ss:
    print(x[1][1])
for x in ns:
    print(x[1][1])
