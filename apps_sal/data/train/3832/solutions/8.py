all_permuted = a = lambda n: (0, 0, 1)[n] if n < 3 else n * a(n - 1) + (-1) ** n
