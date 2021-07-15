def how_much_water(L,X,N):
    if (N > X * 2):
        return 'Too much clothes'
    elif (N < X):
        return 'Not enough clothes'
    else:
        return round(L * ((1 + 0.1) ** (N - X)), 2)
