def binary_cleaner(seq):
    return ([i for i in seq if i <= 1], [i for (i, el) in enumerate(seq) if el > 1])
