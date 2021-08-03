from bisect import bisect_left, bisect
import sys
sys.setrecursionlimit(10 ** 6)  # 変更

n = int(input())
x = list(map(int, input().split()))
L = int(input())
t = n.bit_length()
prv = [n - 1] * n
for i in range(n):
    prv[i] = bisect(x, x[i] + L) - 1
kprv = [prv]
S = prv
for i in range(t - 1):
    kar = [n - 1] * n
    for j in range(n):
        kar[j] = S[S[j]]
    kprv.append(kar)
    S = kar

q = int(input())
for _ in range(q):
    a, b = map(lambda x: int(x) - 1, input().split())
    if a > b:
        a, b = b, a
    lef = 0
    rig = n - 1
    while rig - lef > 1:
        mid = (rig + lef) // 2
        p = mid.bit_length()
        now = a
        for i in range(p):
            if (mid >> i) & 1 == 1:
                now = kprv[i][now]
        if now >= b:
            rig = mid
        elif now < b:
            lef = mid
    print(rig)
