import itertools


def maximum_product_of_parts(n):
    s = str(n)
    return max(
        int(s[:i]) * int(s[i:j]) * int(s[j:])
        for i, j in itertools.combinations(range(1, len(s)), 2)
    )
