import re

SPLITTER = re.compile(r"[\s-]")


def birdify(lst):
    return ''.join(x[:4 // len(lst)] for x in lst) + ('' if len(lst) != 3 else lst[-1][1])


def bird_code(arr):
    return [birdify(SPLITTER.split(name)).upper() for name in arr]
