from itertools import product


def proc_seq(*args):
    res = [int(''.join(s)) for s in set(product(*map(str, args))) if s[0] != '0']
    if len(res) == 1:
        return [1, res[0]]
    return [len(res), min(res), max(res), sum(res)]
