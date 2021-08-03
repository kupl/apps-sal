from itertools import cycle


def interpreter(tape, s):
    a = list(s)
    i = 0  # selector
    for op in cycle(tape):
        if op == '1':
            a[i] = str(1 - int(a[i]))
        else:
            i += 1
            if i == len(s):
                return ''.join(a)
