def max_multiple(divisor, bound):
    valid = []
    for i in range(bound + 1):
        if i % divisor == 0:
            valid.append(i)
    return valid[len(valid) - 1]
