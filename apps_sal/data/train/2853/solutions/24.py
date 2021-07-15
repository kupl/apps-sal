def solve(seq):
    set1 = set()
    seq = list(reversed(seq))
    set_add = set1.add
    return list(reversed([x for x in seq if not (x in set1 or set_add(x))]))
