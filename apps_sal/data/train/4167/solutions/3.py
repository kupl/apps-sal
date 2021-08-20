def descriptions(l):
    return 1 << sum((b - a == 1 for (a, b) in zip(l, l[1:])))
