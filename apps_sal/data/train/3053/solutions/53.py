def close_compare(a, b, margin=0):

    compare = 0

    if margin != 0:
        if a < b and (b - a) <= margin:
            compare = 0
            return compare

        if a < b and (b - a) > margin:
            compare = -1
            return compare

        if a == b:
            compare = 0
            return compare

        if a > b and (a - b) <= margin:
            compare = 0
            return compare

        if a > b and (a - b) > margin:
            compare = 1
            return compare

    else:
        if a < b:
            compare = -1
            return compare
        if a > b:
            compare = 1
            return compare
        if a == b:
            compare = 0
            return compare
