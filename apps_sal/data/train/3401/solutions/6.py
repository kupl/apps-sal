def product(dice): return dice[int()] * product(dice[1:]) if len(dice) > 1 else dice[int()]
def eq_dice(dice): return len(recursive(product(dice), [], [])) - 1 if len(dice) > 1 else len(recursive(product(dice), [], []))


def recursive(num, x, y, dice=3):
    if 3 > num // 3:
        return y
    while dice <= num // dice and dice < 21:
        if num % dice == int():
            if sorted(x + [dice, num // dice]) not in y and num // dice < 21:
                y.append(sorted(x + [dice, num // dice]))
            y = recursive(num // dice, x + [dice], y)
        dice += 1
    return y
