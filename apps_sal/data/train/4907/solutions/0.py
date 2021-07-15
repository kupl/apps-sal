def candles(candles, make_new):
    return candles + (candles - 1) // (make_new - 1)
