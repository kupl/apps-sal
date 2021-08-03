def animals(heads, legs):
    cows = legs / 2 - heads
    chickens = heads - cows
    return (chickens, cows) if (chickens % 1 == 0.0) and (cows % 1 == 0.0) and (chickens >= 0 and cows >= 0) else "No solutions"
