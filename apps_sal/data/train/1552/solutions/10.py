def find_min(m, W):
    i = 1
    while i <= m:
        if i not in W:
            break
        i += 1
    return i


def find_max(M, W, m):
    i = min(M, m)
    while i > 0:
        if i not in W:
            break
        i -= 1
    return i


cache = {}


def knap(M, W, m):
    if len(W) == m or M < find_min(m, W) or M == 0:
        return 0
    if (M, tuple(W), m) in cache:
        return cache[M, tuple(W), m]
    if m * (m + 1) / 2 < M:
        cache[M, tuple(W), m] = m * (m + 1) / 2
        return cache[M, tuple(W), m]
    val = find_max(M, W, m)
    W.add(val)
    cache[M, tuple(W), m] = val + knap(M - val, W, m)
    return cache[M, tuple(W), m]


tests = int(input())
for i in range(tests):
    (n1, n2, m) = [int(x) for x in input().split(' ')]
    W = set()
    M = min(n1, n2)
    print(max(n1, n2) - M + 2 * (M - knap(M, W, m)))
