def close_compare(a, b, margin=0):
    marginal = abs(a - b)
    if margin >= marginal:
        return 0
    if a < b:
        return -1
    if a > b:
        return 1


print(close_compare(2, 8, ))
pass
