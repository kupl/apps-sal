from itertools import compress, product, chain
from functools import partial


def check(f, s):
    if f.is_literal():
        return f in s
    elif f.is_and():
        return all((check(e, s) for e in f.args))
    elif f.is_or():
        return any((check(e, s) for e in f.args))
    elif f.is_not():
        return not check(f.args[0], s)


def get_name(f):
    if f.is_literal():
        yield f
    else:
        yield from chain.from_iterable(map(get_name, f.args))


def sat(f):
    s = set(get_name(f))
    return next(filter(partial(check, f), map(set, map(partial(compress, s), product((0, 1), repeat=len(s))))), False)
