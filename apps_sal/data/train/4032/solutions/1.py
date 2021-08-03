def binomial_coefficient(n, k):
    if not n >= k >= 0:
        return None
    lower_k = min(k, n - k)
    coeff = 1
    for i in range(lower_k):
        coeff *= n - i
        coeff //= i + 1
    return coeff


def catalan_number(n):
    return binomial_coefficient(2 * n, n) // (n + 1)


def solve(n):
    return catalan_number(n)
