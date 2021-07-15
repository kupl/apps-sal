from itertools import groupby

def count_me(data):
    if not data.isdecimal():
        return ""
    groups = ["".join(g) for _, g in groupby(data)]
    return "".join(f"{len(g)}{g[0]}" for g in groups)
