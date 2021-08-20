from itertools import permutations


def equal_to_24(*aceg):
    ops = '+-*/'
    for b in ops:
        for d in ops:
            for f in ops:
                for (a, c, e, g) in permutations(aceg):
                    for s in make_string(a, b, c, d, e, f, g):
                        try:
                            if eval(s + '== 24'):
                                return s
                        except:
                            pass
    return "It's not possible!"


def make_string(a, b, c, d, e, f, g):
    return [f'(({a} {b} {c}) {d} {e}) {f} {g}', f'({a} {b} {c}) {d} ({e} {f} {g})', f'{a} {b} ({c} {d} ({e} {f} {g}))']
