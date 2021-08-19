from itertools import cycle


def cyclic_string(s):
    i = 0
    while True:
        i = s.find(s[0], i + 1)
        if i == -1:
            return len(s)
        if all((c1 == c2 for (c1, c2) in zip(cycle(s[:i]), s[i:]))):
            return i
