
def climb(n):
    res = []
    cur = 1
    mask = 1 << max(0, n.bit_length() - 2)

    while cur <= n:
        res.append(cur)
        cur = 2 * cur + (1 if (n & mask) != 0 else 0)
        mask >>= 1

    return res
