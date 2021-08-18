def transpose(s, i): return (lambda sharp, flat: [sharp[(flat.index(n) + i + 12) % 12] if n in flat else sharp[(sharp.index(n) + i + 12) % 12] for n in s])(["A", "A
