def animals(heads, legs):
    cows = (legs - heads * 2) / 2
    chickens = (legs - cows * 4) / 2
    if cows % 1 != 0 or chickens % 1 != 0 or cows < 0 or (chickens < 0):
        return 'No solutions'
    return (int(chickens), int(cows))
