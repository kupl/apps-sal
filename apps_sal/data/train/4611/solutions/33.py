def animals(heads, legs):
    if heads == 0 and legs == 0:
        return 0, 0
    cows = (legs - heads*2) / 2
    if heads <= 0 or legs <= 0 or cows > heads or cows % 1 != 0 or cows < 0:
        return 'No solutions'
    
    return heads - cows, cows
