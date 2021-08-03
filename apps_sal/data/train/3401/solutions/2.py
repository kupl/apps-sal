from itertools import combinations_with_replacement
from pprint import pprint


def multiples(f):
    m = []
    for i in range(2, 8):
        m.append(combinations_with_replacement(f, i))
    return m


def eq_dice(set_):
    mul = 1
    for e in set_:
        mul *= e
    facts = [x for x in range(3, 21) if not mul % x]
    count = 0
    for r in multiples(facts):
        for m in r:
            mu = 1
            for e in m:
                mu *= e
            if mu == mul and set(m) != set(set_):
                print(m)
                count += 1
    print(count)
    return count
