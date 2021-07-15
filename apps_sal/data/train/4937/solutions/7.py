BASE_BET = 100

def martingale(bank, outcomes, bet = BASE_BET):
    for win in outcomes:
        if win:
            bank += bet
            bet = BASE_BET
        else:
            bank -= bet
            bet *= 2
    
    return bank
