def cycle(seq):
    for (i, n) in enumerate(seq):
        if n in seq[i + 1:]:
            return [i, seq.index(n, i + 1) - i]
    return []
