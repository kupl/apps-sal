def mutually_exclusive(dice, call1, call2):
    dice.sort()
    if sum(pair[1] for pair in dice) != 1:
        return None
    else:
        return '{:.2f}'.format(dice[call1-1][1] + dice[call2-1][1])
