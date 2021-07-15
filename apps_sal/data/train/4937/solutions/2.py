def martingale(bank, outcomes):
    nxt = 100
    for result in outcomes:
        if result:
            bank += nxt
            nxt = 100
        else:
            bank -= nxt
            nxt *= 2
    return bank
