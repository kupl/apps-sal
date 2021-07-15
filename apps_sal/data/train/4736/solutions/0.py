from itertools import chain
def how_many_bees(hive):
        return bool(hive) and sum(s.count('bee') + s.count('eeb') for s in map(''.join, chain(hive, zip(*hive))))
