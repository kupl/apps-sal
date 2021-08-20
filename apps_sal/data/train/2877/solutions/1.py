def count(a, t, y):
    return sum((not (x - t) % y if y else x == t for x in a))
