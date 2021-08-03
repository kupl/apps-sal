memo = {}


def roll_dice(rolls, sides, threshold):
    memo = {}
    r = 0
    for i in range(rolls, threshold):
        r += _roll_dice(rolls, sides, i)
    return 1 - r


def _roll_dice(rolls, sides, s):
    if s < 1:
        return 0
    elif rolls == 1:
        if s > sides:
            return 0
        return 1 / sides
    key = (rolls, sides, s)
    if key in memo:
        return memo[key]
    r = 0
    for i in range(1, sides + 1):
        r += _roll_dice(rolls - 1, sides, s - i)
    memo[key] = r / sides
    return r / sides
