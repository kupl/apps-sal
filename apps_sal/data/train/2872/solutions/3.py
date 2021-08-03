def coin(n): return [x + v for x in coin(n - 1) for v in 'HT'] if n - 1 else ['H', 'T']
