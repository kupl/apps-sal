def egged(year, span):
    if year == 0:
        return 'No chickens yet!'
    egg = []
    for i in range(year):
        egg = [int(e * 0.8) for e in egg]
        egg.append(300)
    return sum(egg[-span:]) * 3
