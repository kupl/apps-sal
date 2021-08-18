a = None


def subsolve(l, r, c):
    nonlocal a
    if r - l <= 1:
        return 0 if a[l] == c else 1
    mid = (l + r) // 2
    u = subsolve(mid, r, c + 1)
    for i in range(l, mid):
        if a[i] != c:
            u += 1
    v = subsolve(l, mid, c + 1)
    for i in range(mid, r):
        if a[i] != c:
            v += 1
    return min(u, v)


def solve():
    nonlocal a
    n = int(input())
    a = list(map(ord, input()))
    print(subsolve(0, n, ord('a')))


t = int(input())
for _ in range(t):
    solve()
