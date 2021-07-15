from itertools import cycle, islice

def endless_string(stg, i, l):
    i = min(i, i+l) % len(stg) + (l < 0)
    j = i + abs(l)
    return "".join(islice(cycle(stg), i, j))
