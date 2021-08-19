import math


def read():
    return list(map(int, input().strip().split()))


def rs():
    return int(input().strip())


t = rs()
ans = []


def find_edges(n, k):
    return min(max_edges(n, k), k)


def max_edges(n, k):
    return (n - k + 1) * (n - k) >> 1


def find(n):
    l = (n >> 1) + n % 2
    r = n
    while l + 1 < r:
        mid = l + (r - l >> 1)
        if max_edges(n, mid) < mid:
            r = mid - 1
        else:
            l = mid
    if max_edges(n, r) >= r:
        return find_edges(n, r)
    else:
        return find_edges(n, l)


for _ in range(t):
    n = rs()
    ans.append(find(n))
print('\n'.join([str(x) for x in ans]))
