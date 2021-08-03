from itertools import combinations_with_replacement
from numpy import prod


def eq_dice(set_):
    lst = sorted(set_)
    eq, dice, count = 0, [], prod(lst)

    for sides in range(3, 21):
        if count % sides == 0:
            dice.append(sides)

    for num_dice in range(2, 8):
        for c in combinations_with_replacement(dice, num_dice):
            if prod(c) == count and sorted(c) != lst:
                eq += 1

    return eq
