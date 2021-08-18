import sys
readline = sys.stdin.readline
read = sys.stdin.read


def isqrt(x):
    ok = 0
    ng = 10**9 + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if mid**2 <= x:
            ok = mid
        else:
            ng = mid
    return ok


def solve(a, b):
    ab = a * b
    if ab == 1:
        return 0
    x = isqrt(a * b - 1)
    if x * (x + 1) < ab:
        res = 2 * x
    else:
        res = 2 * x - 1
    if x >= min(a, b):
        res -= 1
    return res


q = int(readline())
for _ in range(q):
    a, b = list(map(int, readline().split()))
    print((solve(a, b)))
