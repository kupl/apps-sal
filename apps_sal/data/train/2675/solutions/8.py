from itertools import chain, repeat


def mul(x):
    return x[0] * x[1]


def bad_apples(apples):
    inserting = [sum(pair) for pair in apples if mul(pair) == 0 and sum(pair) > 0]
    ins_pairs = chain(chain(*zip(list(zip(*[iter(inserting)] * 2)), repeat(None))), repeat(None))
    return list(filter(bool, [pair if mul(pair) > 0 else list(next(ins_pairs) or ()) for pair in apples if sum(pair) > 0]))
