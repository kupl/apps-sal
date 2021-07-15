from itertools import zip_longest as zl


def combine_strings(*stgs):
    return "".join("".join(z) for z in zl(*stgs, fillvalue=""))
