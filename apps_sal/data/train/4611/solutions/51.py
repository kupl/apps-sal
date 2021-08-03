def animals(heads, legs):
    if heads == 0 and legs == 0:
        return 0, 0
    print(heads, legs)
    if legs > heads * 4 or heads * 2 > legs or heads < 0 or legs < 0 or (legs - heads * 2) % 2 != 0:
        return 'No solutions'
    cows = (legs - (heads * 2)) // 2
    chickens = heads - cows
    return chickens, cows
