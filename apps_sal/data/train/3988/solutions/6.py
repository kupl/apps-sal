from itertools import groupby


def encode(string):
    return "".join([f"{len(list(g))}{k}" for k, g in groupby(string)])


def decode(string):
    number = ""
    result = []
    for i in string:
        if i in "1234567890":
            number += i
        else:
            result += [i] * int(number)
            number = ""
    return "".join(result)
