def round_it(n):
    (a, b) = list(map(len, str(n).split('.')))
    return (int(n) + 1, int(n), round(n))[(a >= b) + (a == b)]
