def russian_peasant_multiplication(x, y, p=0): return p if y == 0 else russian_peasant_multiplication(x + x, y // 2, p if y % 2 == 0 else p + x)
