def is_hollow(x):
    return len(x) > 2 and (x[0] and x[-1] and is_hollow(x[1:-1]) or set(x) == {0})
