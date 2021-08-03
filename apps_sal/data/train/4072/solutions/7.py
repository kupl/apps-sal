def permutation_position(p): return sum(26**i * (ord(c) - 97)for i, c in enumerate(p[::-1])) + 1
