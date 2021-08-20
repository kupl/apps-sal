def same_col_seq(val, k, col):
    results = []
    term = 1
    while values(term) <= val:
        term += 1
    while len(results) < k:
        if colors(values(term)) == col:
            results.append(values(term))
        elif values(term) >= 2 * k * val and len(results) == 0:
            return []
        term += 1
    return results


def values(term):
    if term % 2 == 0:
        return int(term / 2 * term + term / 2)
    else:
        return int((term + 1) / 2 * term)


def colors(term):
    if term % 3 == 0:
        return 'blue'
    else:
        return 'red'
