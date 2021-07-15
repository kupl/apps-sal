def duplicates(lst):
    return sum(lst.count(n) // 2 for n in set(lst))

