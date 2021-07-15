def is_hollow(x):
    while x and x[0] != 0 and x[-1] != 0: x = x[1:-1]
    return len(x) > 2 and set(x) == {0}
