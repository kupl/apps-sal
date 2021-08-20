def how_many_bees(hive):
    if not hive or len(hive) < 3 or len(hive[0]) < 3:
        return 0

    def rn90(a):
        return [list(x) for x in zip(*a[::-1])]

    def r45(a):
        return [[val for (r, row) in enumerate(a) for (c, val) in enumerate(row) if r + c == i][::-1] for i in range(len(a) + len(a[0]))]

    def bees(a):
        return sum((''.join(r).count('bee') for r in a))

    def dbees(a):
        return bees(r45(a))
    result = bees(hive) + bees(rn90(hive)) + bees(rn90(rn90(hive))) + bees(rn90(rn90(rn90(hive))))
    result += dbees(hive) + dbees(rn90(hive)) + dbees(rn90(rn90(hive))) + dbees(rn90(rn90(rn90(hive))))
    return result
