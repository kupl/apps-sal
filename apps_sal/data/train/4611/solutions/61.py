def animals(heads, legs):
    cows = (legs - 2 * heads) / 2
    chickens = heads - cows
    if cows < 0 or chickens < 0 or cows % 1 or chickens % 1:
        return 'No solutions'
    return (chickens, cows)
