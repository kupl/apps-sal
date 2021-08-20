from collections import defaultdict as dd
import math


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


q = nn()
for _ in range(q):
    (n, m, a, b) = mi()
    if not m * b == n * a:
        print('NO')
        continue
    print('YES')
    for i in range(n):
        row = []
        for j in range(m):
            if (a * i + j) % m < a:
                row.append('1')
            else:
                row.append('0')
        print(''.join(row))
