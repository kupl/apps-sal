from itertools import cycle
def zozonacci(seq, n):
    if not n or not seq:return []
    common = {1: [0, 1, 0, 0], 0: [0, 0, 0, 1]}
    ini = common[seq[0] == "pad"]
    if n<=4:return ini[:n]
    fib = lambda:sum(ini[-2:])
    jac = lambda:ini[-1] + 2 * ini[-2]
    pad = lambda:sum(ini[-3:-1])
    pel = lambda:2 * ini[-1] + ini[-2]
    tet = lambda:sum(ini[-4:])
    tri = lambda:sum(ini[-3:])
    for i in cycle(seq):
        ini.append(locals()[i]())
        if len(ini) == n : return ini
