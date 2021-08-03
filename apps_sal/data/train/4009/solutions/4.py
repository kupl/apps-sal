import math


def digits_average(input):
    m = str(input)
    for i in range(len(str(input)) - 1):
        m = ''.join(str(math.ceil(int(m[i]) / 2 + int(m[i + 1]) / 2)) for i in range(len(m) - 1))
    return int(m)
