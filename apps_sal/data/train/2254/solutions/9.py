n, q = map(int, input().split())
l = []
a = [[] for _ in range(n)]
tp = 0
ans = 0
anss = []
for i in range(q):
    x, b = map(int, input().split())
    if x == 1:
        l.append(1)
        a[b - 1].append(len(l) - 1)
        ans += 1
    elif x == 2:
        while len(a[b - 1]) > 0:
            z = a[b - 1].pop()
            ans -= l[z]
            l[z] = 0
    else:
        while tp < b:
            ans -= l[tp]
            l[tp] = 0
            tp += 1
    anss.append(str(ans))
print('\n'.join(anss))
