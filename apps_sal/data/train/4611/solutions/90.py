def animals(heads, legs):
    cows = abs(legs // 2 - heads)
    chickens = abs(cows - heads)
    if cows * 4 + chickens * 2 != legs:
        return 'No solutions'
    return (chickens, cows)
