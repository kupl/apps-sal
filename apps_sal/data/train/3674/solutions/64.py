import math


def add_binary(a, b):
    total = a + b
    bin = ""
    power = int(math.log(total, 2))
    runsum = 0
    while power >= 0:
        if 2**power + runsum <= total:
            bin += "1"
            runsum += 2**power
        else:
            bin += "0"
        power -= 1
    first_1 = bin.index('1')
    return bin[first_1:]
