def mutually_exclusive(dice, call1, call2):
    dice = dict(dice)
    if abs(sum(dice.values()) - 1) < 1e-12:
        return '%0.2f' % (dice[call1] + dice[call2])
