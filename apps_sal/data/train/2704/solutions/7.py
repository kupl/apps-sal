def almost_increasing_sequence(a): return sum((y >= z) * (2 - (x < z))for x, y, z in zip([a[1] - 1] + a[:-3] + [a[-1] - 1], a, a[1:])) < 2
