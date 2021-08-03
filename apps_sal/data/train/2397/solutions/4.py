def solve(mid):
    small = mid
    large = 2 ** m - mid - 1
    for val in s:
        if val < mid:
            small -= 1
        if val > mid:
            large -= 1
    return small < large


def solve2(mid):
    small = mid
    large = 2 ** m - mid - 1
    for val in s:
        if val < mid:
            small -= 1
        if val > mid:
            large -= 1
    return small <= large


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = set([int(input(), 2) for i in range(n)])
    ng = -1
    ok = 2 ** m + 2
    if len(s) % 2 == 0:
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if mid in s:
                for i in range(ng + 1, ok):
                    if i not in s:
                        mid = i
                        break
            if solve(mid):
                ng = mid
            else:
                ok = mid
        print('{:060b}'.format(ng)[::-1][0:m][::-1])
    else:
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if mid in s:
                for i in range(ng + 1, ok):
                    if i not in s:
                        mid = i
                        break
            if solve2(mid):
                ng = mid
            else:
                ok = mid
        print('{:060b}'.format(ng)[::-1][0:m][::-1])
