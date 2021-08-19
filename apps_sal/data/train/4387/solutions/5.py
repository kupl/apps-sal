def sum_no_duplicates(L):
    return sum([n for n in L if L.count(n) == 1])
