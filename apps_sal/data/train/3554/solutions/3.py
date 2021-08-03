def get_score(dice):
    counter = [dice.count(n + 1) for n in range(6)]
    if counter.count(1) == 6:
        return 1000
    if counter.count(2) == 3:
        return 750
    factors = [10, 2, 3, 4, 5, 6]
    result = 0
    for i in range(6):
        if counter[i] >= 3:
            result += (counter[i] - 2) * factors[i] * 100
            counter[i] = 0
    result += counter[0] * factors[0] * 10
    result += counter[4] * factors[4] * 10
    return result or "Zonk"
