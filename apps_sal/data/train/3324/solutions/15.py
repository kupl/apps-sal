def sale_hotdogs(n):
    """
    ## Method 1: Straightforward
    if n < 5:
        return n*100
    elif n > 4 and n < 10:
        return n*95
    elif n > 9:
        return n*90
    """
    '\n    ## Method 2: Reduced Logic\n    if n > 10:\n        return n*90\n    return n*(100-(int(n*.2)*5))\n    '
    return [n * (100 - int(n * 0.2) * 5), n * 90][n > 10]
