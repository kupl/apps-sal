from collections import defaultdict


def interpreter(tape):
    i, res, D = 0, [], defaultdict(int)
    for c in tape:
        if c == '>':
            i += 1
        elif c == '<':
            i -= 1
        elif c == '+':
            D[i] = (D[i] + 1) % 256
        elif c == '*':
            res.append(chr(D[i]))
    return ''.join(res)
