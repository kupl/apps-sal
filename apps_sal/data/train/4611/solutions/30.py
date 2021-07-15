def animals(heads, legs):
    cows = (legs - 2 * heads) / 2
    chickens = heads - cows
    if cows >= 0 and chickens >= 0 and round(cows) == cows:
        return (chickens, cows)
    else:
        return "No solutions"
