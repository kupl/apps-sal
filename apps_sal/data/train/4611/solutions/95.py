def neg_or_float(var):
    return var < 0 or not float(var).is_integer()


def animals(heads, legs):
    cows = 0.5 * legs - heads
    chick = heads - cows
    return 'No solutions' if neg_or_float(cows) or neg_or_float(chick) else (chick, cows)
