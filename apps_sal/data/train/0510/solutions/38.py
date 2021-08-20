from collections import defaultdict
from bisect import bisect, insort, bisect_left
n = int(input())
s = list(input())
q = int(input())
d = defaultdict(list)
for i in range(n):
    d[s[i]] += [i]
for _ in range(q):
    (t, i, c) = input().split()
    (t, i) = (int(t), int(i) - 1)
    if t == 1:
        if s[i] == c:
            continue
        d[s[i]].pop(bisect(d[s[i]], i) - 1)
        s[i] = c
        insort(d[c], i)
    else:
        res = 0
        c = int(c) - 1
        for j in d.values():
            if bisect(j, c) - bisect_left(j, i):
                res += 1
        print(res)
