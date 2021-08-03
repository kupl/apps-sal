def square_up(n): return sum([[0] * (i - 1) + list(range(n, 0, -1))[i - 1:] for i in range(n, 0, -1)], [])
