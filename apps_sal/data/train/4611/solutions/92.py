def animals(heads, legs):
    cows = (legs - heads * 2) / 2
    chickens = heads - cows
    if chickens >= 0 and cows >= 0 and (chickens % 1 == cows % 1 == 0):
        return (chickens, cows)
    else:
        return 'No solutions'
