from itertools import product


def operator_insertor(n):
    op = []
    k = []
    for y in [1, 2, 3, 4, 5, 6, 7, 8]:
        k.append([str(y)])
        k.append(['+', '-', ''])
    k.append(['9'])
    s = product(*k)
    l = []
    for e in s:
        g = ''.join(e)
        if eval(g) == n:
            l.append(len(g) - 9)
            print(g)
    return min(l) if l else None
