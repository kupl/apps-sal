def partition(n, s=2):
    if n <= 1:
        return []
    if n < 4:
        return [[n]]
    ans = []
    while True:
        while n % s != 0:
            s += 1
        if s > n ** 0.5:
            break
        l = [s]
        p = partition(n / s, s)
        for i in p:
            x = sorted(l + i)
            if not x in ans:
                ans += [x]
        ans += [l + [n / s]]
        s += 1
    return ans


def prod_int_part(n):
    p = partition(n)
    return [len(p), min(p) if p else []]
