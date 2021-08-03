def sum_no_duplicates(l):
    return sum([n for n in l if l.count(n) == 1])
