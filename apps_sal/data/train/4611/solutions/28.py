def animals(heads, legs):
    cows = legs / 2 - heads
    chickens = heads - cows
    if cows < 0 or chickens < 0 or cows != int(cows) or (chickens != int(chickens)):
        return 'No solutions'
    return (chickens, cows)
