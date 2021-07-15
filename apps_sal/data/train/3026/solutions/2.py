def min_value(digits):
    l = list(set(digits))
    l.sort(reverse=True)
    return sum(x * 10**i for i, x in enumerate(l))
