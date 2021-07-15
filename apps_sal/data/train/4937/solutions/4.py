def martingale(bank, outcomes):
    loss=win=0
    stake=100
    for i in outcomes:
        if i==1:
            bank+=stake
            if stake!=100:
                stake=100
        else:
            bank-=stake
            stake*=2
    return bank
    #beat the house here...

