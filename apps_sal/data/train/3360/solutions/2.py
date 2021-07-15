def get_chance(shots, laxatives, drinks):
    proba = 1
    for i in range(drinks):
        proba *= 1 - (laxatives / shots)
        shots -= 1
    return round(proba, 2)
