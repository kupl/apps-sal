def partition(n, parts, m=1):
    if parts == 1:
        return [[n]]
    ans = []
    s = m
    while s <= n / parts:
        l = [s]
        p = partition(n - s, parts - 1, s)
        for i in p:
            ans += [l + i]
        s += 1
    return ans


def part_const(n, k, num):
    p = partition(n, k)
    return len([i for i in p if not num in i])
