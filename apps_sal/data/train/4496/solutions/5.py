def hamming_distance(a, b): return sum(1for x, y in zip(a, b)if x != y)
