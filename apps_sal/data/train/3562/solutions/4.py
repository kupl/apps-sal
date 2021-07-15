def count_inversion(sequence):
    return sum(a > b for i, a in enumerate(sequence[:-1]) for b in sequence[i+1:])
