from collections import Counter
from itertools import chain

def repeat_sum(l):
    return sum(key for key, value in Counter(chain.from_iterable(set(x) for x in l)).items() if value > 1)
