def even_numbers_before_fixed(S, p):
    return sum(not e%2 for e in S[:S.index(p)]) if p in S else -1
