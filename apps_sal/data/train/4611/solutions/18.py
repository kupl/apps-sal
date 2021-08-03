def animals(heads, legs):
    cows = (legs - 2 * heads) / 2
    chickens = heads - cows
    if ".5" in str(cows) or cows < 0 or chickens < 0:
        return 'No solutions'
    return (chickens, cows)
