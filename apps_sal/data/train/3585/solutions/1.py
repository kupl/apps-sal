from itertools import product


def proc_seq(*args):
    p = set([int(''.join(e)) for e in product(*[[c for c in str(arg) if i or c != '0'] for i, arg in enumerate(args)])])
    return [len(p)] + ([min(p), max(p)] if len(p) > 1 else []) + [sum(p)]
