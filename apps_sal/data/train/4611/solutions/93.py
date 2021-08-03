def animals(heads, legs):
    chickens = 2 * heads - legs / 2
    cows = legs / 2 - heads
    if chickens < 0 or cows < 0 or not chickens.is_integer() or not cows.is_integer():
        msg = 'No solutions'
    else:
        msg = (chickens, cows)
    return msg
