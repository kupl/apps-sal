from collections import defaultdict
from itertools import cycle


def interpreter(tape):
    (i, skip, D, res) = (0, False, defaultdict(int), [])
    for c in cycle(tape):
        if skip:
            skip = False
        elif c == '>':
            i += 1
        elif c == '<':
            i -= 1
        elif c == '+':
            D[i] = (D[i] + 1) % 256
        elif c == '-':
            D[i] = (D[i] - 1) % 256
        elif c == '*':
            res.append(chr(D[i]))
        elif c == '&':
            break
        elif c == '/':
            skip = not D[i]
        elif c == '\\':
            skip = D[i]
    return ''.join(res)
