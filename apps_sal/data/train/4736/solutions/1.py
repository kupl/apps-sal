def count(it):
    return sum(''.join(x).count('bee') + ''.join(x).count('eeb') for x in it)


def how_many_bees(hive):
    return count(hive) + count(zip(*hive)) if hive else 0
