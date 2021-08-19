def sum_to_infinity(sequence):
    a = sequence[0]
    r = sequence[1] / sequence[0]
    # checking r is in range
    if r <= -1 or r >= 1:  # r mustn't be higher or equal than one and lower or equal minus one
        return "No Solutions"
    else:  # there is formula to counting the sum of infinity geometric sequence
        return round(a / (1 - r), 3)  # rounded to 3 decimal places
