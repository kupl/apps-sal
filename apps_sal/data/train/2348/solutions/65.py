from bisect import bisect_left, bisect_right
import sys
read = sys.stdin.read
readline = sys.stdin.readline

n, = list(map(int, readline().split()))
*x, = list(map(int, readline().split()))
l, q, *ab = list(map(int, read().split()))


M = 19
"""
L = [[bisect_left(x,i-l) for i in x]]
for i in range(M):
    LL = [L[-1][L[-1][i]] for i in range(n)]
    L.append(LL)

"""
R = [[bisect_right(x, i + l) - 1 for i in x]]
for i in range(M):
    RR = [R[-1][R[-1][i]] for i in range(n)]
    R.append(RR)


mp = iter(ab)
for a, b in zip(mp, mp):
    a -= 1
    b -= 1
    if a > b:
        a, b = b, a

    ans = 0
    for i in range(M, -1, -1):
        if R[i][a] < b:
            ans += 1 << i
            a = R[i][a]
    print((ans + 1))
