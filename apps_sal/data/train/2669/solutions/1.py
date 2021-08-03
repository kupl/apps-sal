def next(base):
    mul = 1
    for c in str(base):
        if c != "0":
            mul *= int(c)
    return base + mul


def convergence(n):
    base = 1
    test = n
    count = 0
    while test != base:
        if test > base:
            base = next(base)
        else:
            test = next(test)
            count += 1
        print(str(base) + " " + str(test))
    return count
