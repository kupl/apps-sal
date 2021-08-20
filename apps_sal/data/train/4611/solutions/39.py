def animals(heads, legs):
    cows = legs // 2 - heads
    chickens = heads - cows
    return (heads - cows, cows) if heads >= 0 and legs >= 0 and (legs % 2 == 0) and (cows >= 0) and (chickens >= 0) else 'No solutions'
