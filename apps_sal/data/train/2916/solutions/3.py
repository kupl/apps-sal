def mutually_exclusive(dice, call1, call2):
    prob = 0
    tprob = 0
    for i in dice:
        if i[0] == call1 or i[0] == call2:
            prob += i[1]
        tprob += i[1]
    return '{:.2f}'.format(prob) if tprob == 1 else None
