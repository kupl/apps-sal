import itertools
import collections


def slogan_maker(array):
    return [' '.join(i) for i in itertools.permutations(collections.OrderedDict.fromkeys(array))]
