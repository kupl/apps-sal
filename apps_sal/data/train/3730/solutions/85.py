def capitalize(s):
    x = list(s)
    y = [x[n].upper() if n % 2 == 0 else x[n] for (n, i) in enumerate(x)]
    z = [x[n].upper() if n % 2 == 1 else x[n] for (n, i) in enumerate(x)]
    return [''.join(y), ''.join(z)]
