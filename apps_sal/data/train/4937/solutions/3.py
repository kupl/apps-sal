def martingale(n, a, m=100):
    return sum(((y := (x and m or -m)) and (m := (x and 100 or m * 2)) and y for x in a)) + n
