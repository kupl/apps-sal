def magic_sum(a):
    return sum((n % 2 * n * ('3' in str(n)) for n in a or []))
