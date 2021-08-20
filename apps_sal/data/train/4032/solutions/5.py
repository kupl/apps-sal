def binomial(n, k):
    (n, k) = (int(n), int(k))
    if not n >= k >= 0:
        return None
    k = min(k, n - k)
    product = 1
    for i in range(k):
        product *= n - i
        product //= i + 1
    return product


def catalan(n):
    return binomial(2 * n, n) // (n + 1)


def solve(n):
    return catalan(n)
