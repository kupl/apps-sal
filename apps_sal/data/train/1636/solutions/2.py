def productsum(n):
    return sum(set(factors[2:n + 1]))


def _productsum(prod, sum, n, start):
    k = prod - sum + n
    if k > k_max:
        return
    if prod < factors[k]:
        factors[k] = prod
    for i in range(start, 2 * k_max // prod + 1):
        _productsum(prod * i, sum + i, n + 1, i)


k_max = 12000
factors = [2 * k_max] * (k_max + 1)
_productsum(1, 1, 1, 2)
