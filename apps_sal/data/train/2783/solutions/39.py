from collections import OrderedDict


def get_grade(*s):
    avg = sum(s) / len(s)
    for (a, g) in zip([60, 70, 80, 90], ['F', 'D', 'C', 'B']):
        if avg < a:
            return g
    return 'A'
