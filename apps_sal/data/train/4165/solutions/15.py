from functools import reduce
def uni_total(string):
    return reduce(lambda x, y: x + ord(y), string, 0)
