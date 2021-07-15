def martingale(bank, outcomes):
    risking = 100
    for outcome in outcomes:
        if outcome == 0:
            bank -= risking
            risking *= 2
        if outcome == 1:
            bank += risking
            risking = 100
    return bank
