def sale_hotdogs(n):
    if n < 5:
        cost = 100*n
    elif n < 10:
        cost = 95*n
    else:
        cost = 90*n
    return cost
