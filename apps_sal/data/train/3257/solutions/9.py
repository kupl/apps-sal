from collections import Counter
from itertools import permutations


def slogan_maker(array):
    slogan = [i for i in list(Counter(array).keys())]
    res = []
    for i in permutations(slogan, len(slogan)):
        res.append(" ".join(i))
    return res
