def hex_to_dec(n):
    n = list(n.lower())
    n = [10 if x == 'a' else 11 if x == 'b' else 12 if x == 'c' else 13 if x == 'd' else 14 if x == 'e' else 15 if x == 'f' else int(x) for x in n]
    Tsum = 0
    p = 0
    for (p, i) in enumerate(reversed(n), p):
        Tsum = Tsum + i * 16 ** p
    return Tsum
