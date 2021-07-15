def count_fours(n, base):
    fours = 0
    while n > 0:
        if n % base == 4:
            fours += 1
        n //= base
    return fours

def int_to_str_in_base(n, base):
    result = ""
    while n > 0:
        result = str(n % base) + result if n % base < 10 else "x" + result
        n //= base
    return result

def fouriest(i):
    highscore = 0
    winner = 5
    for base in range(5, i-3, 1):
        fours = count_fours(i, base)
        if fours > highscore:
            highscore = fours
            winner = base
        elif 4*base**(highscore) > i:
            break
    result = int_to_str_in_base(i, winner)
    return "{} is the fouriest ({}) in base {}".format(i, result, winner)
