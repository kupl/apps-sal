def animals(heads, legs):
    if heads == 0 and legs == 0:
        return (0, 0)

    chickens = (4 * heads - legs) / 2

    cows = heads - chickens

    all_good = chickens.is_integer() and chickens >= 0 and cows >= 0

    return (chickens, cows) if all_good else 'No solutions'
