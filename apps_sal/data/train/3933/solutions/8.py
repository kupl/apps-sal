def hydrate(drink_string):
    n = 0
    for i in range(len(drink_string)):
        try:
            n += int(drink_string[i])
        except:
            continue
    if n == 1:
        return '1 glass of water'
    else:
        return str(n) + ' glasses of water'
