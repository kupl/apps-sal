def animals(heads, legs):
    chickens = heads - (legs - heads * 2) / 2
    cows = (legs - heads * 2) / 2
    if heads == 0 and legs == 0:
        return (0, 0)
    elif chickens.is_integer() and chickens >= 0 and cows.is_integer and (cows >= 0):
        return (chickens, cows)
    else:
        return 'No solutions'
