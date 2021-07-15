def validate_sequence(seq):
    diff = seq[1] - seq[0]
    for i,n in enumerate(seq[:-1]):
        if seq[i + 1] - n != diff:
            return False
    return True
