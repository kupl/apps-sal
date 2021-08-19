#!/usr/bin/env	python
# -*-coding:utf-8 -*-
import sys
import collections
n, q = map(int, input().split())
M = collections.defaultdict(collections.deque)
Q = collections.deque()
L = []
s = n = m = 0
for _ in range(q):
    y, x = map(int, input().split())
    if 2 > y:
        s += 1
        Q.append(x)
        M[x].append(n)
        n += 1
    elif 3 > y:
        y = M.get(x)
        if y:
            s -= len(y)
            del M[x]
    else:
        while x > m:
            z = Q.popleft()
            y = M.get(z)
            if y and y[0] < x:
                s -= 1
                y.popleft()
                if not y:
                    del M[z]
            m += 1
    L.append(s)
sys.stdout.write('\n'.join(map(str, L)))
