def animals(heads, legs):
    if heads == legs == 0:
        return (0, 0)
    if heads < 0 or legs < 0 or legs % 2 == 1:
        return 'No solutions'
    for i in range(heads + 1):
        cows = i * 4
        chickens = (heads - i) * 2
        if legs == chickens + cows:
            return (chickens / 2, cows / 4)
    return 'No solutions'
