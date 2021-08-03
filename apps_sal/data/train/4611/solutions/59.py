def animals(heads, legs):
    cows = (legs - 2 * heads) / 2
    chickens = heads - cows

    if cows < 0 or chickens < 0 or heads < 0 or legs < 0:
        return "No solutions"
    elif cows != int(cows):
        return "No solutions"
    else:
        return (chickens, cows)
