from itertools import starmap


def number(lines):
    return list(starmap("{}: {}".format, enumerate(lines, 1)))
