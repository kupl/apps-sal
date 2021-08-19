def min_value(digits):
    a = []
    for i in range(len(digits)):
        if digits[i] not in a:
            a.append(digits[i])
    return int(''.join((repr(n) for n in sorted(a))))
