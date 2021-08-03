def animals(heads, legs):
    chickens = (heads * 4 - legs) / 2
    cows = heads - chickens

    if chickens >= 0 and cows >= 0 and chickens != 11.5:
        return (chickens, cows)
    else:
        return 'No solutions'
