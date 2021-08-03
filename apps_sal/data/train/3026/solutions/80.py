def min_value(digits):
    list = []
    for x in sorted(set(digits)):
        if x > 0:
            list.append(x)
    return int(''.join(map(str, list)))
