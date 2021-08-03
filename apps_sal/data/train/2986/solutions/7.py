def segments(m, a):
    segments = {n for l, r in a for n in range(l, r + 1)}
    return [n for n in range(m + 1) if n not in segments]

# one-liner: [n for n in range(m+1) if n not in {n for l, r in a for n in range(l, r+1)}]
