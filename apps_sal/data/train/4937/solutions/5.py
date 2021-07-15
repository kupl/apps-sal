def martingale(bank, outcomes, rate = 100):
    for i in outcomes:
        bank -= rate
        if i:
            bank += rate*2
            rate = 100
        else:
            rate *= 2
    return bank
