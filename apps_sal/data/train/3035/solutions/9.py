def getMatrixProduct(a, b):
    """If a and b can be multiplied, returns the product of a and b as a two-dimensional array. Otherwise returns -1."""
    (arl, acl) = (len(a), len(a[0]))
    (brl, bcl) = (len(b), len(b[0]))
    if acl != brl:
        return -1

    def row(ar, n):
        return ar[n]

    def col(ar, n):
        return [r[n] for r in ar]

    def prod_sum(ar1, ar2):
        return sum((v1 * v2 for (v1, v2) in zip(ar1, ar2)))
    return [[prod_sum(row(a, r), col(b, c)) for c in range(bcl)] for r in range(arl)]
