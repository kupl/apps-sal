def vampire_test(x, y):
    return "".join(sorted(list(str(x) + str(y)))) == "".join(sorted(list(str(x * y))))
