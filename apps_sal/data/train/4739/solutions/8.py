def same_col_seq(val, k, col):
    code = {'blue': 0, 'red': 1, 'yellow': 2}
    result = []
    limit = 2 * k * val
    term = 1
    temp = 1
    while temp <= val:
        temp = temp + term + 1
        term += 1
    while True:
        if temp % 3 == code[col]:
            result.append(temp)
        temp = temp + term + 1
        term += 1
        if len(result) >= k:
            break
        if len(result) == 0 and temp >= limit:
            return []
    return result
