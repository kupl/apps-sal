def isPP(n):
    (m, k) = (2, 2)
    while m ** 2 <= n:
        while m ** k <= n:
            if m ** k == n:
                return [m, k]
            else:
                k += 1
        m += 1
        k = 2
    return None
