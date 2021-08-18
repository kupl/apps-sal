def do_sum(m):
    return ((m + 1) * (m + 2)) // 2 - 1


def bin_search(n, l, h):
    m = (l + h) // 2
    if do_sum(m) < n and do_sum(m + 1) >= n:
        return m
    if do_sum(m) < n:
        return bin_search(n, m + 1, h)
    return bin_search(n, l, m - 1)


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    m = bin_search(n, 1, 10000000000)
    print(n - ((m + 1) * (m + 2)) // 2)
