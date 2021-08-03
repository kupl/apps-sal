# cook your dish here
from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    d = defaultdict(int)
    for i in range(n):
        s = input()
        for k in s:
            if k in "codechef":
                d[k] = d[k] + 1
    d['c'] = d['c'] // 2
    d['e'] = d['e'] // 2
    g = list(d.values())
    if len(g) == 6:
        print(min(g))
    else:
        print(0)
