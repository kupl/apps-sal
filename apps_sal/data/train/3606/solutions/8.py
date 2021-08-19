def find_pattern(seq):
    (n, diffs) = (len(seq) - 1, [b - a for (a, b) in zip(seq, seq[1:])])
    for l in range(1, n + 1):
        if n // l * diffs[:l] == diffs:
            return diffs[:l]
