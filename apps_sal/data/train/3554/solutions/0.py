def get_score(dice):
    if all(i in dice for i in range(1, 7)):
        return 1000
    if len(dice) == 6 and all(dice.count(d) == 2 for d in set(dice)):
        return 750
    score = 0
    score += sum((dice.count(d) == n) * d * (n - 2) * (1000 if d == 1 else 100) for d in set(dice) for n in range(3, 7))
    score += 100 * dice.count(1) if dice.count(1) < 3 else 0
    score += 50 * dice.count(5) if dice.count(5) < 3 else 0
    return score if score else 'Zonk'
