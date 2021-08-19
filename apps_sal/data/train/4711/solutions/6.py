def find_factor(p, n):
    """Find how many times the prime number p divides n!"""
    (result, power) = (0, p)
    while power < n:
        result += n // power
        power *= p
    return result


def zeros(n):
    """Find the number of trailing zeroes in n!."""
    return min((find_factor(p, n) for p in (2, 5)))
