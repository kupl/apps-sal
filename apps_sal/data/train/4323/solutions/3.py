def uniq(seq):
    return [c for (i, c) in enumerate(seq) if i == 0 or seq[i - 1] != c]
