def bin_mul(m, n):
    result = []
    ma, mi = max(m, n), min(m, n)
    while(ma != 0):
        if ma % 2 and mi != 0:
            result = [mi] + result
        mi *= 2
        ma //= 2
    return result
