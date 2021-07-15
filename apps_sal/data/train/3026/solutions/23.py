def min_value(a):
    a = list(dict.fromkeys(a))
    a.sort()
    a = int(''.join(map(str, a)))
    return a
