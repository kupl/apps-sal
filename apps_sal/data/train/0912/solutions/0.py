import sys
input = sys.stdin.readline
inp, ip = lambda: int(input()), lambda: [int(w) for w in input().split()]


def check(mid):
    pos = x[0]
    ct = 1
    for i in range(1, n):
        if x[i] - pos >= mid:
            pos = x[i]
            ct += 1
            if ct == k:
                return True
    return False


for _ in range(inp()):
    n, k = ip()
    x = ip()
    x.sort()
    ans = -1
    l, r = 1, x[-1]
    while l < r:
        mid = (l + r) // 2
        if check(mid):
            ans = max(ans, mid)
            l = mid + 1
        else:
            r = mid
    print(ans)
