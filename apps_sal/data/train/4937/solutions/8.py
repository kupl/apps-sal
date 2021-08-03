def martingale(bank, outcomes):
    balance = bank
    stake = 100
    for win in outcomes:
        if win:
            balance += stake
            stake = 100
        else:
            balance -= stake
            stake *= 2
    return balance
