def get_ages(add, dif):
    return None if any(n < 0 for n in (add, dif, add - dif)) else ((add + dif) / 2, (add - dif) / 2)
