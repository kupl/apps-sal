def min_value(digits):
    a = sorted(set(digits))
    b = []
    for i in range(len(a)):
        b.append(str(a[i]))
    return int(''.join(b))
