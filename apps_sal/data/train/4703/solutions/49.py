def bar_triang(*p):  # points A, B and C will never be aligned
    return list([round(sum(x) / 3, 4) for x in zip(*p)])  # coordinates of the barycenter expressed up to four decimals
    # (rounded result)
