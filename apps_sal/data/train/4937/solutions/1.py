def martingale(bank, outcomes):
    bet=100
    for results in outcomes:
        if not bool(results):
            bank= bank -bet
            bet*=2
        if bool(results):
            bank=bank+bet
            bet=100
    return bank
