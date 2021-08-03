from itertools import product


def proc_seq(*li):
    un = {int(''.join(i)) for i in list(product(*map(str, li))) if i[0] != '0'}
    return [1, un.pop()] if len(un) == 1 else [len(un), min(un), max(un), sum(un)]
