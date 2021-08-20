def animals(heads, legs):
    if heads < 0 or legs < 0:
        return 'No solutions'
    else:
        cows = legs / 2 - heads
        chickens = heads - cows
    if chickens < 0 or cows < 0:
        return 'No solutions'
    elif chickens.is_integer() == False or cows.is_integer() == False:
        return 'No solutions'
    else:
        return (chickens, cows)
