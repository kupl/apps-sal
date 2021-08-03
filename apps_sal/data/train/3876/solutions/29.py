def sum_naturals(n): return n * (n + 1) // 2
def sum_multiples(n, m): return m * sum_naturals(n // m)


def find(n):
    return sum_multiples(n, 3) + sum_multiples(n, 5) - sum_multiples(n, 15)
