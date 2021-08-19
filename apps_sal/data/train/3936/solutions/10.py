from itertools import cycle


def zozonacci(seq, n):
    if not n or not seq:
        return []
    common = {1: [0, 1, 0, 0], 0: [0, 0, 0, 1]}
    ini = common[seq[0] == 'pad']
    if n <= 4:
        return ini[:n]

    def fib():
        return sum(ini[-2:])

    def jac():
        return ini[-1] + 2 * ini[-2]

    def pad():
        return sum(ini[-3:-1])

    def pel():
        return 2 * ini[-1] + ini[-2]

    def tet():
        return sum(ini[-4:])

    def tri():
        return sum(ini[-3:])
    for i in cycle(seq):
        ini.append(locals()[i]())
        if len(ini) == n:
            return ini
