def sum_no_duplicates(l):
    return sum((x for x in set(l) if l.count(x) < 2))
