def min_value(digits):
    temp = sorted(list(set(digits)))
    for i in range(len(temp)):
        temp[i] = str(temp[i])
    return int(''.join(temp))
