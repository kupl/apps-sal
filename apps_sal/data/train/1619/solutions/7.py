def decompose(n):
    return decompose_helper(n ** 2, n - 1)


def decompose_helper(n, end):
    for i in range(end, 0, -1):
        if i ** 2 == n:
            return [i]
        new = n - i ** 2
        d = decompose_helper(new, min(i - 1, int(new ** 0.5)))
        if d:
            return d + [i]
