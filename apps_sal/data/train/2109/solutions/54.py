import sys

input = sys.stdin.readline
Q = int(input())

def max_score(x, a):
    ret = 0
    for p in [(x-4), (x-2), x, (x+2), x+4]:
        p += x%2
        p //= 2
        ret = max(ret, (p+(p>=a))*(x-p+1))
    return ret

for _ in range(Q):
    a, b = list(map(int, input().split()))
    a, b = min(a, b), max(a, b)

    def is_ok(x):
        return a*b > max_score(x, a)

    def bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    ans = bisect(2*b+1, a-1)
    print(ans)

