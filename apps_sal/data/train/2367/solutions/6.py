from collections import *


def f(s):
    c = Counter(s)
    if c.most_common()[0][1] > 1:
        return c
    return (c, sum((s[i] > s[j] for i in range(len(s)) for j in range(i, len(s)))) & 1)


for _ in range(int(input())):
    (n, s, t) = (input(), input(), input())
    print('YNEOS'[f(s) != f(t)::2])
