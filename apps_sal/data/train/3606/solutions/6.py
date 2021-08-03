def find_pattern(seq):
    xs = [b - a for a, b in zip(seq, seq[1:])]
    return next((
        xs[:i]
        for i in range(1, len(xs) // 2 + 1)
        if xs[:i] * (len(xs) // i) == xs
    ), xs)
