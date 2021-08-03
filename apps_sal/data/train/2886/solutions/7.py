import re


def find(s):
    x = []
    for g in re.finditer(r"\?+!+", s):
        x.append((len(g[0]), -g.start(), g[0]))
    for g in re.finditer(r"!+\?+", s):
        x.append((len(g[0]), -g.start(), g[0]))
    return max(x)[-1] if x else ""
