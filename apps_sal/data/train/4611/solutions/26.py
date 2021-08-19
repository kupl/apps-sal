def animals(heads, legs):
    chickens = 2 * heads - legs / 2
    cows = legs / 2 - heads
    if legs >= heads >= 0 and chickens >= 0 and (cows >= 0) and (chickens == chickens // 1) and (cows == cows // 1):
        return (chickens, cows)
    else:
        return 'No solutions'
