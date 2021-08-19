def decompose(n):
    res = [0, 0, n]
    for (i, p) in enumerate((3, 2)):
        while not n % p:
            res[i] += 1
            n //= p
    res[0] = -res[0]
    return res


def solve(arr):
    return [n for (_, _, n) in sorted(map(decompose, arr))]
