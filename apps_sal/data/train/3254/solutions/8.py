def any_odd(x):
    return '1' in list(bin(x)[-2::-2])
