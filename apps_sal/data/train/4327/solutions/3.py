def chameleon(C, d): return (lambda a, b, c: -1if a == c < 1 or (b - a) % 3else b)(*sorted([C[i]for i in (0, 1, 2)if i != d]) + [C[d]])
