sum_naturals = lambda n: n * (n + 1) // 2
sum_multiples = lambda n, m: m * sum_naturals(n // m)

def find(n):
    return sum_multiples(n, 3) + sum_multiples(n, 5) - sum_multiples(n, 15)
