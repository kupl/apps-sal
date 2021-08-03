def animals(heads, legs):
    if neg_or_float(heads) or neg_or_float(legs) or heads > 1000 or legs > 1000:
        return 'No solutions'

    cows = 0.5 * legs - heads
    chick = heads - cows
    return 'No solutions' if neg_or_float(cows) or neg_or_float(chick) else (chick, cows)


def neg_or_float(var):
    return var < 0 or not float(var).is_integer()
