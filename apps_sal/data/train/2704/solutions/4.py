def almost_increasing_sequence(sequence):
    prev = sequence[0] - 1
    n = 0
    for i, x in enumerate(sequence):
        if x <= prev:
            if n:
                return False
            n = 1
            if i > 1 and sequence[i - 2] >= x:
                continue
        prev = x
    return True
