def sum_to_infinity(sequence):
    r = sequence[2]/sequence[1]
    if not -1 < r < 1:
        return "No Solutions"
    return round(sequence[0]/(1-r),3)
