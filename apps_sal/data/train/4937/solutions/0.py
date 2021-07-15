def martingale(bank, outcomes):
    stake = 100
    for i in outcomes:
        if i == 0:
            bank -= stake
            stake *= 2
        else:
            bank += stake
            stake = 100
    return bank
