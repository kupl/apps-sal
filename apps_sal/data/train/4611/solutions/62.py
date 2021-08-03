def animals(heads, legs):
    if heads < 0 or legs < 0:
        return 'No solutions'
    cows = (legs - 2 * heads) / 2
    chickens = (4 * heads - legs) / 2
    if cows < 0 or chickens < 0:
        return 'No solutions'
    if int(cows) != cows or int(chickens) != chickens:
        return 'No solutions'
    else:
        return (int(chickens), int(cows))
