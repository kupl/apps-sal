def find_longest(xs):
    return max(xs, key=lambda x: len(str(x)))
