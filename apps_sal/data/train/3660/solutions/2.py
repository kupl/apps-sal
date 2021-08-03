count_paths = lambda n, C, f=__import__('math').factorial: (n != 1) * f(n + C[0] - 1 - C[1]) // f(C[0]) // f(n - 1 - C[1])
