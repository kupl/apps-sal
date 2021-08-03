def candles(m, n):
    burnt = m
    leftovers = m
    while leftovers // n >= 1:
        burnt += leftovers // n
        leftovers = leftovers % n + leftovers // n
    return burnt
