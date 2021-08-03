import math


def round_it(n):
    print(n)
    test = str(n)
    counter = 0
    for val in test:
        if val == ".":
            break
        counter += 1
    if counter > (len(test) - 1) / 2:
        return math.floor(float(test))
    elif counter < (len(test) - 1) / 2:
        return math.ceil(float(test))
    else:
        return round(float(test))
