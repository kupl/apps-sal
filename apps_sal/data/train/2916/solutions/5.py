def mutually_exclusive(dice, call1, call2):
    dice = {a: b for a, b in dice}
    return None if sum(dice.values()) != 1 else f'{float(dice[call1] + dice[call2]):.02f}'

