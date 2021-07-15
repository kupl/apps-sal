def nbr_of_laps(x, y):
    for i in range(min(x, y), 0, -1):
        if x % i == 0 and y % i == 0:
            break
    return (y / i, x / i)

