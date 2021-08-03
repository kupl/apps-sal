def animals(heads, legs):
    # return (Chickens, Cows)
    if heads == 0 and legs == 0:
        return (0, 0)
    elif heads < 0 or legs < 0:
        return 'No solutions'
    else:
        result = False
        chickens = 0
        cows = 0
        for i in range(heads + 1):
            if i * 2 + (heads - i) * 4 == legs:
                result = True
                chickens = i
                cows = heads - i

        if result:
            return (chickens, cows)
        else:
            return 'No solutions'
