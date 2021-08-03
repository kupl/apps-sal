def powers_of_two(n): return [1]if n == 0 else powers_of_two(n - 1) + [2**n]
