import itertools
import collections

def reg_sum_hits(num_dice, sides):
    rollsums = [sum(x) for x in itertools.product([side for side in range(1,sides+1)],repeat=num_dice)]
    return [ [k,v] for k,v in sorted( collections.Counter(rollsums).items() ) ]

