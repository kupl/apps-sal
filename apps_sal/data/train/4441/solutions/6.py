from functools import reduce
from operator import or_

SHIFTS = {'user': 6, 'group': 3, 'other': 0}

def chmod_calculator(perm):
    return format(reduce(or_, (
        (('r' in p) << 2 | ('w' in p) << 1 | ('x' in p)) << SHIFTS[user]
        for user, p in perm.items()
    ), 0), '03o')
