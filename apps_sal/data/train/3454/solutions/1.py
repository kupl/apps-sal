def candies_to_buy(n):
    xx = 1
    for i in range(n):
        x = xx
        while xx % (i + 1):
            xx += x
    return xx
