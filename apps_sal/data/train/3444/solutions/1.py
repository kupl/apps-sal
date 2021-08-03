import math


def cyclic_string(s):
    for l in [i for i, ch in enumerate(s) if ch == s[0]][1:]:
        if (s[:l] * math.ceil(len(s) / l))[:len(s)] == s:
            return l
    return len(s)
