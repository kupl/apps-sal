from itertools import permutations


def get_words(d):
    return sorted([''.join(i) for i in set(list(permutations(''.join([''.join([k * i for k in j]) for (i, j) in d.items()]))))])
