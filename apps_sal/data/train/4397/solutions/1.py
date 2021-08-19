def is_thue_morse(seq):
    return all((bin(i).count('1') % 2 == n for (i, n) in enumerate(seq)))
