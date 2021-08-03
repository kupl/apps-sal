def binary_cleaner(seq):
    return [n for n in seq if n < 2], [i for i, n in enumerate(seq) if n > 1]
