def find_missing(sequence):
    """Identify the missing element in an arithmetic expression
    following a constant rule
    """
    # A linear list of differences between each element in sequence.
    dif = [sequence[x + 1] - sequence[x] for x in range(len(sequence) - 1)]

    # An array of individual elements and their frequency in dif; [[element, frequency],]
    dif_freq = [[x, dif.count(x)] for x in set(dif)]

    # Sorting by ascending frequency
    sorted_dif_freq = sorted(dif_freq, key=lambda x: x[1])

    outlier = sorted_dif_freq[0][0]
    constant = sorted_dif_freq[-1][0]

    return sequence[dif.index(outlier)] + constant
