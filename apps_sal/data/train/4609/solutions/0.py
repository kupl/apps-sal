def egged(year, span):
    total = 0
    eggs_per_chicken = 300
    for i in range(min(span, year)):
        total += 3 * eggs_per_chicken
        eggs_per_chicken = int(eggs_per_chicken * 0.8)
    return total or 'No chickens yet!'
