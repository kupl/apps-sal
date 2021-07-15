def buy_or_sell(pairs, want):
    r = []
    for buy, sell in pairs:
        if want not in [buy, sell]: return 'ERROR'
        r, want = (r + ['buy'], sell) if buy == want else (r + ['sell'], buy)
            
    return r  
