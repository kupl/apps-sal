import numpy
base = [1]


def convergence(n):
    test = [n]
    while test[-1] not in base:
        if base[-1] > test[-1]:
            test.append(test[-1] + int(numpy.prod([int(dig) for dig in str(test[-1]) if int(dig) != int()])))
        else:
            base.append(base[-1] + int(numpy.prod([int(dig) for dig in str(base[-1]) if int(dig) != int()])))
    return len(test) - 1
