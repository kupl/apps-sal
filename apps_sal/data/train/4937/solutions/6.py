def martingale(bankRoll, outcomes):
    baseBet = 100
    betMultiplier = 1

    for i in outcomes:
        if i:  # we won: Update our bank roll, reset our bet to the base case of 100
            bankRoll += betMultiplier * baseBet
            betMultiplier = 1
        else:  # we lost: Update our bank roll,  double our previous bet
            bankRoll -= betMultiplier * baseBet
            betMultiplier *= 2

    return bankRoll
# end martingale function
