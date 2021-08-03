import re


def shortest_to_char(s, c):
    if not c or c not in s:
        return []
    positions = [m.start() for m in re.finditer(c, s)]
    return [min(abs(p - i) for p in positions) for i in range(len(s))]
