def animals(heads, legs):
    if legs % 2 != 0:
        return 'No solutions'
    chickens = 2 * heads - legs // 2
    cows = heads - chickens
    return (chickens, cows) if chickens >= 0 and cows >= 0 else 'No solutions'
