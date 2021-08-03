from itertools import groupby


def count_me(s):
    return "".join(str(sum(1 for _ in y)) + x for x, y in groupby(s)) if s.isdigit() else ""
