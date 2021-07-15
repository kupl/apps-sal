def vampire_test(x, y):
    return (x > 0 or y > 0) and sorted(str(x) + str(y)) == sorted(str(x * y))
