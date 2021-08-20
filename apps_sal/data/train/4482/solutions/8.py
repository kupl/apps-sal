def even_numbers_before_fixed(seq, e):
    return sum((1 - n % 2 for n in seq[:seq.index(e)])) if e in seq else -1
