def sum_to_infinity(sequence):
    sum = 0
    print(sequence)
    if len(sequence) > 1:
        r = sequence[1] / sequence[0]
        print(r)
        if r <= -1 or r >= 1:
            return 'No Solutions'
        sum = round(sequence[0] / (1 - r), 3)
        return sum
    return sequence[0]
