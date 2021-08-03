from functools import reduce


def resistor_parallel(*res):
    # it take an unlimited number of arguments
    # create the function resistor_parallel

    return 1 / reduce(lambda x, y: x + y, [1 / x for x in res])
