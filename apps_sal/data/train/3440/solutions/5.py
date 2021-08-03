def powers(n): return [1 << i for i in range(n.bit_length())if 1 << i & n]
