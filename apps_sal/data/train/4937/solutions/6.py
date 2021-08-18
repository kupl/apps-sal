def martingale(bankRoll, outcomes):
    baseBet = 100
    betMultiplier = 1

    for i in outcomes:
        if i:
            bankRoll += betMultiplier * baseBet
            betMultiplier = 1
        else:
            bankRoll -= betMultiplier * baseBet
            betMultiplier *= 2

    return bankRoll
