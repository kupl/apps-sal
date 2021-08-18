"""
Created on Tue Apr 23 17:13:53 2019

@author: avina
"""


def digit_sum(n):
    d = 0
    while n:
        d += n % 10
        n //= 10
    return d


for _ in range(int(input())):
    n, d = map(int, input().strip().split())

    q = []
    ma = {}
    q.append((n, 0))
    i = 0
    while i < 10000 and len(q) != 0:
        t = q.pop(0)
        if t[0] < 10:
            if t[0] in ma:
                continue
            else:
                ma[t[0]] = t[1]
        else:
            q.append((digit_sum(t[0]), t[1] + 1))

        q.append((t[0] + d, t[1] + 1))
        i += 1
    k = sorted(list(ma.keys()))
    print(k[0], ma[k[0]])
