def animals(heads, legs):
    chickens = 2 * heads - legs / 2
    cows = legs / 2 - heads
    if heads < 0 or legs < 0 or chickens < 0 or (cows < 0):
        return 'No solutions'
    elif heads == legs == 0:
        return (0, 0)
    elif chickens.is_integer() and cows.is_integer():
        return (2 * heads - legs // 2, legs // 2 - heads)
    else:
        return 'No solutions'
