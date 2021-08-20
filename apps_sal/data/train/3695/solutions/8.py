import re
from itertools import groupby


def repeat_adjacent(s):
    return sum((x and next(y) and bool(next(y, 0)) for (x, y) in groupby((x[0] for x in re.findall('((.)\\2*)', s)), key=lambda x: len(x) > 1)))
