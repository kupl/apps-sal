def close_compare(a, b, margin=0):
    plus = a + margin
    minus = a - margin
    if plus > b and minus > b:
        return 1
    elif plus < b and minus < b:
        return -1
    else:
        return 0
