def dating_range(a): return "{}-{}".format(int(a - 0.1 * a if a <= 14 else a / 2 + 7), int(a + 0.1 * a if a <= 14 else (a - 7) * 2))
