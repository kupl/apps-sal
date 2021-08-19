def any_odd(x):
    bina = bin(x).split('b')[1]
    for (a, b) in enumerate(bina, start=len(bina) - 1):
        if a % 2:
            if '1' in b:
                return 1
    return 0
