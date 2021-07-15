def egged(year, span):
    eggs = [300]
    while len(eggs) < span:
        eggs.append(eggs[-1] // 1.25)
    chickens = [3] * year + [0] * span
    return sum(c * e for c, e in zip(chickens, eggs)) if year else 'No chickens yet!'
