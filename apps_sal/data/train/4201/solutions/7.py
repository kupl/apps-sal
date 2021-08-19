def find_missing(sequence):
    """Identify the missing element in an arithmetic expression
    following a constant rule
    """
    dif = [sequence[x + 1] - sequence[x] for x in range(len(sequence) - 1)]
    dif_freq = [[x, dif.count(x)] for x in set(dif)]
    sorted_dif_freq = sorted(dif_freq, key=lambda x: x[1])
    outlier = sorted_dif_freq[0][0]
    constant = sorted_dif_freq[-1][0]
    return sequence[dif.index(outlier)] + constant
