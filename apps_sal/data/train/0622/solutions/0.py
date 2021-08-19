# cook your dish here folding paper
from collections import Counter
def li(): return [int(i) for i in input().rstrip('\n').split()]
def st(): return input().rstrip('\n')
def val(): return int(input().rstrip('\n'))
def dist(a, b): return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5


for _ in range(val()):
    n, m, w, h = li()
    s = Counter(st())
    l = []
    for i in range(m):
        l.append(li())
    ans = float('inf')
    l.sort(key=lambda x: x[0])
    for j in range(1, 50):
        for i in range(j, m):
            ans = min(ans, dist(l[i - j], l[i]))
    for i in l:
        if s['D'] or s['U'] > 1:
            ans = min(ans, 2 * i[1])
        if s['U'] or s['D'] > 1:
            ans = min(ans, 2 * (h - i[1]))
        if s['L'] or s['R'] > 1:
            ans = min(ans, 2 * i[0])
        if s['R'] or s['L'] > 1:
            ans = min(ans, 2 * (w - i[0]))
    print(ans)
