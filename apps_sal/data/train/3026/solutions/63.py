def min_value(digits):
    result = []
    l = [i for i in set(digits)]
    while len(l) > 0:

        result.append(str(l.pop(l.index(min(l)))))

    return int(''.join(result))
