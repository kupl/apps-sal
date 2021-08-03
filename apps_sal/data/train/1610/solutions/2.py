subsets_parity = s = lambda n, k: n < k and "EVEN" or n < 2 and "ODD" or (lambda b: s(n & ~b, k & ~b))(1 << n.bit_length() - 1)
