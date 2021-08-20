def sum_no_duplicates(l):
    return sum((n for n in set(l) if l.count(n) == 1))
