def is_valid(cows, chickens):
    return cows.is_integer() and chickens.is_integer() and (cows >= 0) and (chickens >= 0)


def animals(heads, legs):
    cows = legs / 2 - heads
    chickens = heads - cows
    return (chickens, cows) if is_valid(cows, chickens) else 'No solutions'
