def any_odd(n):
    return 1 if '1' in bin(n)[2:][-2::-2] else 0
