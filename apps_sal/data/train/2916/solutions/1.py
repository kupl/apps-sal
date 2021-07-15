def mutually_exclusive(dice, call1, call2):
    if sum(prob for _, prob in dice) != 1:
        return None
    x = dict(dice)
    return format(x[call1] + x[call2], '.2f')
