def is_magical(sq):
    sums = '123 456 789 147 258 369 159 357'.split()
    return all(check(sq,x) == 15 for x in sums)
def check(sq, entries):
    return sum(sq[x-1] for x in map(int,entries))
